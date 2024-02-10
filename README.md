# Face and Hand Recognition

FaceAndHandRecognition is an innovative project that combines the power of face recognition and hand tracking to enhance security measures and enable intuitive gesture-based actions. 

## Description

This project aims to provide a seamless and secure user experience by leveraging face recognition as a security parameter and utilizing hand tracking for gesture-based control. The system ensures that only authorized individuals have access to its functionalities by employing face recognition for authentication.

Once authenticated, users can interact with the system through hand gestures, which are tracked and recognized by the technology. Currently, the system supports basic actions such as copy, paste, and select all. However, there are plans to expand the range of available actions in future iterations.

## Key Features

- Face recognition for secure authentication
- Hand tracking for gesture-based control
- Support for basic actions like copy, paste, and select all
- Intuitive and hands-free user interface
- Plans for future development and expansion of actions

## Installation

To use the FaceAndHandRecognition project, follow these steps:

1. Clone the repository: `git clone https://github.com/HorizonChaser12/FaceAndHandRecognition.git`
2. Install the required dependencies: `pip install -r requirements.txt`
3. Set up the necessary hardware devices (e.g., camera, hand tracking sensor).
4. Place the images of the faces you want to recognize in the Images folder.
   Update the path variable in the script to the path of the Images folder on your system.
   The script will open the webcam feed and start recognizing hand gestures and faces.
5. Run the project: `python hand_gesture_and_face_recognition.py`.
- Perform various hand gestures to trigger different actions.
- If a recognized face is detected, it will display the name associated with the face.
- If a face is not recognized, it will prompt for a password to gain access.

## Troubleshooting

- If the script is not recognizing your hand gestures properly, try adjusting the min_detection_confidence and min_tracking_confidence parameters in the hands = 
 mpHands.Hands() function.
- Make sure the lighting conditions are suitable for accurate hand and face detection.
- If you get some issues while installing Face-Recognition Module then unzip the [dlib-master.zip](https://github.com/HorizonChaser12/FaceAndHandRecognition/blob/main/dlib-master.7z) and read the instructions.

## Future Development

This project is actively under development, and future plans include:

- Adding more advanced hand gestures and corresponding actions
- Improving the accuracy and efficiency of face recognition and hand tracking algorithms
- Enhancing the user interface and overall user experience
- Integrating with other systems and applications for broader functionality

Contributions and suggestions are welcome! Feel free to open issues and submit pull requests to help improve the project.

## Acknowledgements

We would like to express our gratitude to the developers and contributors of the following libraries and frameworks that made this project possible:

- OpenCV
- TensorFlow
- and other open-source projects used in this project.
