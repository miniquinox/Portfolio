using UnityEngine;
using UnityEngine.Playables;

public class GenericTrigger : MonoBehaviour 
{
	public PlayableDirector timeline;

	// Initialization
	void Start() 
	{
		timeline = GetComponent<PlayableDirector>();
	}
		

	void OnTriggerExit(Collider c)
	{
		if (c.gameObject.tag == "Player") 
		{
			timeline.Stop();
		}
	}

	void OnTriggerEnter(Collider c)
	{
		if (c.gameObject.tag == "Player")
		{
			timeline.Play();
		}
	}
}