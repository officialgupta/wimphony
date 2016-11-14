using UnityEngine;
using System.Collections;

public class Movement : MonoBehaviour, IGvrGazePointer {

	public float mSpeed;

	// Use this for initialization
	void Start () {
		mSpeed = 7f;
	}
		
	// Update is called once per frame
	//void Update () {
	//	transform.Translate(mSpeed * Input.GetAxis ("Horizontal") * Time.deltaTime, 0f, mSpeed * Input.GetAxis ("Vertical") * Time.deltaTime);
	//}
	public void OnGazeStart(Camera camera, GameObject targetObject, Vector3 intersectionPosition, bool isInteractive){return;}
	public void GetPointerRadius(out float innerRadius, out float outerRadius){
		outerRadius = innerRadius = 0;
		return;
	}
	public void OnGazeEnabled(){
		GazeInputModule.gazePointer = this;
		return;
	}
	public void OnGazeDisabled(){return;}
	public void OnGazeStay(Camera camera, GameObject targetObject, Vector3 intersectionPosition, bool isInteractive){return;}
	public void OnGazeTriggerStart(Camera camera) {
		Debug.Log ("GO ON NOW", camera); // Debug the trigger. 
		//transform.Translate (0f, 0f, mSpeed * Time.deltaTime);
	}

	public void OnGazeTriggerEnd(Camera camera) {
		Debug.Log ("GO OFF NOW", camera); // Debug the release of the trigger.
		//transform.Translate (0f, 0f, 0f);
	}

	public void OnGazeExit(Camera camera, GameObject targetObject){return;}	


}