import cv2
import argparse
import json

def list_webcams():
    index = 0
    arr = []
    while True:
        cap = cv2.VideoCapture(index)
        if not cap.read()[0]:
            break
        else:
            properties = {
                "Device ID": index,
                "Frame Width": cap.get(cv2.CAP_PROP_FRAME_WIDTH),
                "Frame Height": cap.get(cv2.CAP_PROP_FRAME_HEIGHT),
                "FPS": cap.get(cv2.CAP_PROP_FPS),
            }
            arr.append(properties)
        cap.release()
        index += 1
    return arr

def capture_image(device_index, output_file):
    cap = cv2.VideoCapture(device_index)

    if not cap.isOpened():
        print(f"Cannot open camera with index {device_index}")
        return

    ret, frame = cap.read()
    if ret:
        cv2.imwrite(output_file, frame)
        print(f"Image captured and saved to {output_file}")
    else:
        print("Failed to capture image")

    cap.release()

def main():
    parser = argparse.ArgumentParser(description="Webcam Capture Script")
    parser.add_argument('--list', action='store_true', help="List all webcam devices and their properties")
    parser.add_argument('--capture', type=int, help="Capture image from the specified camera index")
    parser.add_argument('--output', type=str, default='captured_image.jpg', help="Output file for the captured image")
    args = parser.parse_args()

    if args.list:
        webcams = list_webcams()
        print("Available webcams:")
        print(json.dumps(webcams, indent=4))
    elif args.capture is not None:
        capture_image(args.capture, args.output)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()