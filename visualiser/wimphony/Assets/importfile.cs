using UnityEngine;
using System.Collections;

public class importfile : MonoBehaviour {
	private string _url = "http://www.music.helsinki.fi/tmt/opetus/uusmedia/esim/a2002011001-e02.wav";
	//private string _url = "http://www.wimphony.com/music?field=one&q=eh";
	private AudioClip _audio;

	IEnumerator Start() {
		WWW www = new WWW(_url);
		// Wait for download to complete
		yield return www;
		// get text
		//WWW www2 = new WWW(www.text);
		// Wait for download to complete
		//yield return www2;
		// get text
		//_audio = www2.GetAudioClip(false, false);
		_audio = www.GetAudioClip(false, false);

		AudioSource audio = GetComponent<AudioSource> ();
		audio.clip = _audio;
		audio.spatialBlend = 1;
		audio.loop = true;
		audio.transform.position = new Vector3(Random.value*4,Random.value*4,Random.value*4);
		audio.Play();
	}
}


;