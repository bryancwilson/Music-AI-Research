# Music-AI-Research
 
This github repository serves as a portfolio of my independent undergraduate research conducted from May 2021 to August 2022 at NC State University. I first want to give a huge thanks to the professors and graduate students at NC State University for providing mentorship, guidance, and support during my research effort. I have listed their names below... 

#### May 2021 - August 2021
- **Dr. John-Paul Ore** (Professor in the Dept. of Computer Science at NC State University)

#### May 2021 - Present
- **Dr. Thomas Price** (Professor in the Dept. of Computer Science at NC State University)
- **Jimmy Skripchuck** (Computer Science PhD Student at NC State University)

Also, during both Summer 2021 and Summer 2022, I conducted research through the **Women and Minority Summer Research Program** headed by **Dr. Javon Adams** (Interim Director of the 
College of Engineering Women and Minority Engineering Programs at NC State University).

### Preface
Though I have split these two these research projects into two main stretches, they both can be thought of as one long research project where I explored one main topic
-- computer generated art through machine learning. As a musician, I believe music to be a carefully constructed reflection, by a composer, songwriter, filmscorer, etc., of the human experience. It is both the spontaneity and predictibility throughout a piece of music that embodies a person's life. Futhermore it is the experiences of a person's life which informs the music composition process. Music therefore cannot be mimicked but rather must be learned. 

With the recent 21st century surge in technological advancements, Machine Learning has become a widely researched and implemented tool in organization globally. Naturally within the ongoing conversation regarding the capacity of machine learning, the task of creating art has arisen. There has been success using natural language processing techniques and other generative architectures to compose music, however there is still compositional cielings such as originality and complexity we have not broken through as well as a large mistrust of AI composers from the musician population. 

If quantifying the complexity of human emotions and emulating that in music is unfeasible for a computer, can we instead use machine learning and mathematical concepts to instead model the human composition process which is driven by the human experience. If not, will even a partial or incomplete model lead to much more original and complex sounding music. This ultimately is what I looked to explore in this research project.

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
It is common for path planning problems that utilize Machine Learning to employ Reinforcement Learning techniques. For step wise music composition, I decided to this approach would be most suitable as stepwise composition following a strict criteria can be viewed as analogous to finding the optimal path. For this project I designed my own environment and reward function in addition to employing a Q-Learning Model. Below, I go into more detail in addition to including code snippets and visualizations regarding my methodology.

#### Environment
One of the necessary components for a reinforcement learning model is an environment. An environment is a model of the conditions for which the agents must learn through taking actions given a certain state. For this project I choose a grand staff (treble and bass cleff) in 4/4 time signature and the key of C major for simplicity and readability. I also only included 7 beats for the entire piece having the last beat contain a quarter rest. This was to ensure that the permutations of chords would not explode and become intractible. The first chord was given while all subsequent beats only consisted of a melody and bass note. This results in a total of 6 states as the agent starts on the 2nd beat and ends on the 7th beat.  

```
# RL Environment
class MusicComposition:
    def __init__(self, tonality, timesig, n1, n2, n3, n4, n5, n6, n7): 
        self.PieceInit(tonality, timesig, n1, n2, n3, n4, n5, n6, n7)
        self.stateSpace = [i for i in range(6)] 
        self.stateSpace.remove(5)
        self.stateSpacePlus = [i for i in range(6)]
        self.actionSpaceIndex = {'A3': 1, 'B3': 2, 'C4': 3, 'D4': 4, 'E4': 5, 'F4': 6, 'G4': 7, 'A4': 8, 'B4': 9, 'C5': 10, 'D5': 11, 'E5': 12, 'F5': 13, 'G5': 14, 'A5': 15}
        self.actionSpaceIndexRev = {1: 'A3', 2: 'B3', 3: 'C4', 4: 'D4', 5: 'E4', 6: 'F4', 7: 'G4', 8: 'A4', 9: 'B4', 10: 'C5', 11: 'D5', 12: 'E5', 13: 'F5', 14: 'G5', 15: 'A5'}
        self.actionRangeNum = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        self.noteRange = ['A3', 'B3', 'C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4', 'C5', 'D5', 'E5', 'F5', 'G5', 'A5']
        self.possibleActions = self.makeActionSpace(self.actionRangeNum, self.actionRangeNum, self.actionRangeNum)
        self.actionSpaceNum = [i for i in range(len(self.possibleActions))]
        self.actionSpaceDic = self.makeActionSpaceDict(self.possibleActions, self.actionSpaceNum)
        self.agentPosition = chord.Chord('C4 G4 E5')
        self.initPosition = chord.Chord('C4 G4 E5')
        self.currentState = 0
```

#### Q-Learning
I utilized an e-greedy temporal difference off policy Q-Learning Algorithm. 

#### Reward Function
It would've been infeasible to create an effective reward function based on general musci theory due to its intractible breadth. Therfore I chose to construct a reward function solely on jazz harmonic theory. 

This works utilizes an e-greedy temporal difference off policy Q Learning Algorithm. The Environment consists of a pre written bass 
and melody line with a starting chord for reference. The algorithm has an action space of 72 chords and can only choose one chord per 
beat. Each episode only consists of 6 beats. Because generalizing all of music theory into a reward structure is unfeasible, I based my 
reward model on jazz harmonic theory.


```
print("Hello World")
```

### Results
![Figure_1](https://user-images.githubusercontent.com/84595669/187099460-7961f601-67f0-49a4-ad72-58478871a967.png)

### Conclusions
Unless the algorithm ran for an extremely long time, and the policy gradient descent randomly started at the right initiation, the algorithm wold never find the the optimal policy and would always produce a music composition with errors. E-greedy policy improvement is insufficient to train AI intelligence algorithms to produce original music. 

### Poster
![Slide1](https://user-images.githubusercontent.com/84595669/187097304-0efd3ff1-eab1-403a-8a7c-46b58623d2d0.PNG)

### Citations

## Summer 2022
### Abstract
When approaching the AI problem of generating music compositions, it has become common practice 
to train a supervised learning model on a large corpus of already existing music, usually all within a 
similar music style. Not only does this make the generation of complex music composition much more 
feasible, but it also results in very stable neural models. However, this approach limits the originality and 
complexity of produced compositions. This is largely because supervised learning models analyze the 
training data superficially; learning musical patterns and note structures before generating its own. This 
study seeks to heighten the complexity and originality of AI generated music by training a generative machine learning model 
on a much more abstract musical framework - harmonic consonance and dissonance. By creating a new chord vocabulary
through this abstract musical framework, I will train a transformer model to produce new compositions with greater originality and complexity.

### Methodology
#### Dissonance Curve
![DIssonance Curve Flow Chart](https://user-images.githubusercontent.com/84595669/188961931-74bf63b5-cda7-4e01-a1f6-6694bab8d15a.png)




#### Chord Embeddings


### Results
Currently in Progress

### Conclusions
Currently in Progress

### Poster
![Machine Learning Composing Music Utilizing Frequency Theory pptx](https://user-images.githubusercontent.com/84595669/187098383-ebdfc6a3-73e7-4f1c-9d07-ac7b98ba280c.png)

### Citations

