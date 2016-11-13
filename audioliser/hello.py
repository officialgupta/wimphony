import pdb
import random
import pysynth_b as psb

#generates a wav file based on the streangth and names of available wifi networks
def generate_a_wav_file(list_of_networks):
    wav_file = []

    for network in list_of_networks:
        process_input_values(network)

        for i in range(10):
            wav_file.append(generate_note())
    return wav_file


#processes input values of location, wifi network names
#and wifi strength
def generate_scale(start_note):
    scale_int = [2,2,1,2,2,2,1]

    return reduce(next_note, scale_int, [start_note])

def next_note(acc, intval):
    all_notes = ['a', 'a#', 'b', 'c', 'c#','d', 'd#', 'e', 'f', 'f#', 'g', 'g#']
    acc.append(
        all_notes[
            (all_notes.index(acc[-1]) + intval) % len(all_notes)
        ]
    )
    return acc


def process_input_values(network):

    ssid = network[0]
    ssid_hashed = hash(ssid)
    random.seed(ssid_hashed)
    return ssid_hashed

#generates random numbers from the input
def generate_note():
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

def create_and_save_wav(list_of_networks, url):

    wav = generate_a_wav_file(list_of_networks)

    psb.make_wav(wav, fn = url + ".wav", leg_stac = .7, bpm = 250)


if __name__ == "__main__":
    list_of_networks = ["eduram"]
    url = "testie"
    create_and_save_wav(list_of_networks, url)


