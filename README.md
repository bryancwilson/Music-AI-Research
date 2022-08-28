# Music-AI-Research
 
This github repository serves as a portfolio of my independent undergraduate research from May 2021 to August 2022 conducted at Nc State University. I first want to give a huge thank you to the professors and graduate students at NC State University for their mentorship, guidance, and support. I have listed their names below... 

#### May 2021 - August 2021
- **Dr. John-Paul Ore** (Professor in the Dept. of Computer Science at NC State University)

#### May 2021 - Present
- **Dr. Thomas Price** (Professor in the Dept. of Computer Science at NC State University)
- **Jimmy Skripchuck** (Computer Science PhD Student at NC State University)

Also, during both Summer 2021 and Summer 2022, I conducted research through the **Women and Minority Summer Research Program** headed by **Dr. Javon Adams** (Interim Director of the 
College of Engineering Women and Minority Engineering Programs at NC State University).

### Preface

## Summer 2021
### Abstract
The creation of original music through Artificial Intelligence is not a novel idea. In fact, conceptions of musical automata and automatic music machines are centuries old. 
Due to the seemingly infeasible task of generalizing and quantifying musical structure (harmonic, melodic, and rhythmic structure), researchers have trained their AI algorithms on a dataset
of sheet music using generative supervised Learning. Because the purpose of generative supervised learning is to synthesize new creations based on any given dataset, this approach 
blinds the AI architecture from musical possibilities outside the dataset, thus limiting its originality. The purpose of this study is to broaden the musical possibilities an AI algorithm can 
choose from by instead training a reinforcement learning model through a musical ‘rubric’. Instead of looking to create a sufficient and comprehensive 
reward structure based on the entirety of music, the researcher constructed a reward structure quantified on a much smaller musical structure based entirely on diatonic jazz harmony. This 
reward structure will be used to train the reinforcement learning model. It is expected that by taking this approach, the reinforcement learning model will synthesize music at 
a higher level of originality then that of generative supervised learning models. 

### Methodology
This works utilizes an e-greedy temporal difference off policy Q Learning Algorithm. The Environment consists of a pre written bass 
and melody line with a starting chord for reference. The algorithm has an action space of 72 chords and can only choose one chord per 
beat. Each episode only consists of 6 beats. Because generalizing all of music theory into a reward structure is unfeasible, I based my 
reward model on jazz harmonic theory.

### Results
### Conclusions
### Poster
![Slide1](https://user-images.githubusercontent.com/84595669/187097304-0efd3ff1-eab1-403a-8a7c-46b58623d2d0.PNG)

### Citations

## Summer 2021
### Abstract
When approaching the AI problem of generating music compositions, it has become common practice 
to train a supervised learning model on a large corpus of already existing music, usually all within a 
similar music style. Not only does this make the generation of complex music composition much more 
feasible, but it also results in very stable neural models. However, this approach limits the originality and 
complexity of produced compositions. This is largely because supervised learning models analyze the 
training data superficially; learning musical patterns and note structures before generating its own. This 
study seeks to heighten the complexity and originality of AI generated music by training a generative machine learning model 
on a much more abstract musical framework - harmonic consonance and dissonance. By creating a new chord vocabulary
through this abstract musical framework, I can train a transformer model to produce new compositions with greater originality and complexity.

### Methodology
#### Dissonance Graph for 2 Voice Chords
![Dissonance_Curve_Interval](https://user-images.githubusercontent.com/84595669/187098097-bf4dcc70-a830-4147-a027-1005b2d6b52d.png)


#### Dissonance Graph for 3 Voice Chords
![Dissonance_Curve_Chords](https://user-images.githubusercontent.com/84595669/187098092-c7da87aa-83d7-439c-b5de-b7488e55f1df.png)


#### Dissonance Graph for 4 Voice Chords
![Dissonane_Curve_Seventh](https://user-images.githubusercontent.com/84595669/187098102-44edea67-53cb-46c0-8fac-970622367f31.png)


### Results
Currently in Progress

### Conclusions
Currently in Progress

### Poster
![Machine Learning Composing Music Utilizing Frequency Theory pptx](https://user-images.githubusercontent.com/84595669/187098383-ebdfc6a3-73e7-4f1c-9d07-ac7b98ba280c.png)

### Citations
