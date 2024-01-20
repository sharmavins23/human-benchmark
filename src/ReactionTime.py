import mss
from icecream import ic
import mouse

# ===== Constants ==============================================================

pixelPosition = (800, 300)
redColor = (165, 30, 43)
greenColor = (30, 151, 80)
blueColor = (34, 108, 167)

# ===== Driver Code ============================================================


def main():
    # Loop until we decide to stop
    while True:
        # Take a screenshot of the pixel to get the pixel's color
        with mss.mss() as screenshot:
            picture = screenshot.grab({
                'mon': 1, 
                'top': pixelPosition[1], 
                'left': pixelPosition[0], 
                'width': 1, 
                'height': 1
            })
            rgbVal = picture.pixel(0,0)
        
        # Check if the pixel is green
        if rgbVal == greenColor:
            # If it is, move to the pixel location
            mouse.move(pixelPosition[0], pixelPosition[1], absolute=True)
            # Then click
            mouse.click(button='left')



if __name__ == "__main__":
    main()