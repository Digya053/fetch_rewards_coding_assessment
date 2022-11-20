# fetch_rewards_coding_assessment
This program calculates the equally-spaced pixel coordinate values to be displayed on a 2D surface given the dimensions of the image and its corner points.

# Running the program:

The quickest way to view the output is through the heroku URL: [https://fetch-rewards-assessment.herokuapp.com/](https://fetch-rewards-assessment.herokuapp.com/)

![image](https://drive.google.com/uc?export=view&id=1TP-ilTpufQ_pepUF3_nGWFPAzqth1R89)

The <b>Image Dimension</b> field contains entry for number of rows and columns of a 2D array which is set to 0 by default, and the <b>Corner Points</b> field contains the textbox for the four corner points of an array.
Additionally, another input textbox for <b>Number of values after decimal</b> have been added with default value of 2 to give users the flexibility to produce output with their desired number of values after the decimal. 

For instance, the example input dimension of ```(3, 3)``` and corner points ```[(1, 1), (3, 1), (1, 3), (3, 3)]``` can be added to the UI in their respective position and then, submitted as shown in the image below:
![image](https://drive.google.com/uc?export=view&id=1Nfbup_zXXDjMgp02hf0imxrf-As5fsa2)

## Steps to run the program:

1. Clone the repository.
2. Go inside fetch_rewards_coding_assessment folder.
3. Start docker.
4. Build docker image: ```docker image build -t fetch-rewards .```
5. Run image: ```docker run -p 5000:5000 -d fetch-rewards```

The above UI will then, be available at [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

For running the python file directly and testing using the above example:

1. Clone the repository.
2. Go inside fetch_rewards_coding_assessment folder.
3. Create a virtual environment and run ```pip3 install -r requirements.txt```
4. Run ```python3 -m src.pixel_coordinates --corner_pts="[(1,1),(3,1),(1,3),(3,3)]" --n_rows=3 --n_cols=3 --n_decimal=2```









