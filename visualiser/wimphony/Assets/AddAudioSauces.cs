using UnityEngine;
using System.Collections;

public class AddAudioSauces : MonoBehaviour {

	// Use this for initialization
	void Start () {
		AudioSource audio = gameObject.AddComponent<AudioSource>();
		audio.clip = Resources.Load("music") as AudioClip;
		audio.transform.position = new Vector3(0, 1, -2);
		audio.spatialBlend = 1;
		audio.Play();
	}
	
	// Update is called once per frame
	void Update () {
	
	}
}
