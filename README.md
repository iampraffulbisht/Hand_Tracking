Hand Tracking with MediaPipe

<img width="1278" alt="Screenshot 2024-06-10 at 1 43 30 AM" src="https://github.com/iampraffulbisht/Hand_Tracking/assets/114369813/8842d11d-51ac-4e2c-a06d-7b05d281992b">

<img width="523" alt="Screenshot 2024-06-10 at 1 40 04 AM" src="https://github.com/iampraffulbisht/Hand_Tracking/assets/114369813/d3180086-d674-47fd-8c9f-966372c8527f">


This project demonstrates real-time hand tracking using MediaPipe, a powerful machine learning framework for building multi-modal applications. By leveraging MediaPipe's Hands solution, you can detect and visualize hand landmarks in a video stream, making it suitable for various interactive experiences.

Prerequisites

To run this project, you'll need the following software installed on your desktop:

Python 3.x: Download and install Python from the official website (https://www.python.org/downloads/).
pip: pip is the package installer for Python. If you installed Python correctly, pip should be included. You can verify its installation by running python -m pip --version in your terminal.
Dependencies

The project relies on the following Python libraries:

opencv-python: For video capture, image processing, and display. Install it using pip install opencv-python.
mediapipe: For hand landmark detection. Install it using pip install mediapipe.
Installation

Clone the Repository:
Open a terminal or command prompt and navigate to your desired project directory. Then, clone this repository using the following command:

Bash
git clone https://github.com/iampraffulbisht/Hand_Tracking
Use code with caution.

Replace your-username with your actual GitHub username.

Install Dependencies:
Navigate to the cloned project directory using:

Bash
cd hand-tracking-with-mediapipe
Use code with caution.

Then, install the required dependencies using pip:

Bash
pip install opencv-python mediapipe
Use code with caution.



Running the Project

Execute the Script:
Run the main Python script using the following command:

Bash
python hand_tracking.py
Use code with caution.

This will launch a webcam window displaying your hand with detected landmarks visualized as circles and connections.

Terminate the Application:
Stop termianl to  terminate application 

Customization (Optional)

FPS Display: You can modify the script to display the frames per second (FPS) for performance monitoring.
Landmark Colors: You can change the colors used to draw circles and connections on the hand landmarks.
Advanced Interactions: Explore integrating hand tracking with other functionalities, such as mouse control or gesture recognition.
Additional Notes

Ensure you have a webcam connected to your computer for the video stream.
Adjust the webcam resolution settings if you encounter performance issues.
