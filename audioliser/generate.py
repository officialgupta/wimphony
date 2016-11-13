import random
import pysynth_b as psb

def generate_abc_notation(network):
    """ Generates a sequence of notes that
        can then be used by pysynth to
        generate a wav file
    """
    ssid = network[0]
    ssid_hashed = hash(ssid)
    random.seed(ssid_hashed)

    notes = [generate_note() for i in range(30)]

    return notes

def generate_scale(start_note):
    """ Generates a scale of notes from a start note """
    scale_int = [2,2,1,2,2,2,1]

    return reduce(next_note, scale_int, [start_note])

def next_note(acc, intval):
    """ Function used by generate scale
        takes an accumulator which is a list of all the
        notes already in the scale and the next interval
        From this it generates the next note in the scale
        and returns it appended to acc
    """
    all_notes = ['a', 'a#', 'b', 'c', 'c#','d', 'd#', 'e', 'f', 'f#', 'g', 'g#']
    acc.append(
        all_notes[
            (all_notes.index(acc[-1]) + intval) % len(all_notes)
        ]
    )
    return acc

def generate_note():
    """ Generates a note in ABC notation suitable
        for passing to pysynth
    """
    all_notes = ['a', 'a#', 'b', 'c', 'c#','d', 'd#', 'e', 'f', 'f#', 'g', 'g#']
    scale_int = [2,2,1,2,2,2,1]
    list_of_tempos = [9, 16, 36, 64]
    tempo = random.choice(list_of_tempos)

    list_of_note_lengths = [1, 2, 2, 2, 4, 4, 8, 16]

    scale = str(random.randint(3, 5))
    length = random.randrange(1, 4)

    starting_note = random.choice(all_notes)

    note = random.choice(generate_scale(starting_note))

    return ((note + scale), length)

def create_and_save_wav(list_of_net_name_pairs):
    """ Main function """
    list_of_wavs = []
    for net_name_pair in list_of_net_name_pairs:

        network, url = net_name_pair
        wav = generate_abc_notation(network)

        wav_file = psb.make_wav(wav, fn = url + ".wav", leg_stac = .7, bpm = 350)
        list_of_wavs.append(wav_file)

    return list_of_wavs

if __name__ == "__main__":
    list_of_net_name_pairs = [("eduram", "testie")]
    create_and_save_wav(list_of_net_name_pairs)


