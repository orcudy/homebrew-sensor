import RPi.GPIO as GPIO
import time
import socket
import sys
import os
import utils


def send_state(state, host, port):
    try:
        print("Sending state: " + str(int_to_bool(state)))
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host, port))
        sock.sendall("post " + str(int_to_bool(state)))
    except Exception as exception:
        print("Failed to send state: " + str(exception))

def cleanup():
    print("Cleaning up.")
    GPIO.cleanup()

def main():
    if len(sys.argv) != 4:
        print("Usage: sensor <host> <port> <shared_secret>")
        print("For more info: https://github.com/orcudy/homebrew-sensor")
        sys.exit()

    host = sys.argv[1]
    if !utils.is_domain_name(host) and !utils.is_ipv4_address(host):
        print("Invalid host. (Host must be domain name or ipv4 address.)")
        sys.exit()

    port = int(sys.argv[2])
    if !utils.is_valid_port(port):
        print("Invalid port number. (Port must be between 1024 and 65535.)")
        sys.exit()
        
    probe = 13
    detector = 11
    
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(probe, GPIO.OUT)
    GPIO.setup(detector, GPIO.IN)

    try:
        #initialize prev_state to current state
        prev_state = GPIO.input(detector)

        #sample forever
        while (True):
            #set probe output HIGH indefinitely
            GPIO.output(probe, 1)
        
            cur_state = GPIO.input(detector)
            print cur_state

            #if state change, inform server
            if (prev_state != cur_state):
                prev_state = cur_state
                send_state(cur_state)
                
            #sample once per minute
            time.sleep(1) #sampling every second for testing
        
    except Exception as exception:
        print("Recieved the following exception: " + exception)
        cleanup()

    except KeyboardInterrupt:
        print("Keyboard Interrupt!")
        cleanup()

if __name__ == "__main__":
    main()    
