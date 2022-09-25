# Music-AI-Research
 
##### NOTE
Coding files will be uploaded pending research paper publications. This portfolio is also subject to change as my research continues to progress and evolve.

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
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
-- **computer generated art through machine learning**. As a musician, I believe music to be a carefully constructed reflection, by a composer, songwriter, filmscorer, etc., of the human experience. It is both the spontaneity and predictability throughout a piece of music that embodies a person's life. Furthermore it is the experiences of a person's life which informs the music composition process. Music composition therefore cannot be mimicked but rather must be learned. 

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
For the Q-Learning implementation, I utilized an E-Greedy Temporal Difference Off Policy Q-Learning Algorithm. To break this title up, e-greedy stands for epsilon-greedy and is essentially an approach at handling the exploration/exploitation problem in Machine Learning. In the beggining of the iterative learning process, a value called epsilon is set to a constant C where 0 < C < 1. For every episode (a sequence of states until completion of the task) epsilon is decreased until the last few episodes are reached where it reaches its lowest value. During every episode a random number N where 0 < N < 1 is generated and compared to the current value of C. If N > C, a random action from the action space is chosen (exploration). If N < C then to action with the current highest Q-Value is chosen (exploitation). As learning continues, the best actions will be chosen more often because C is decreasing. Temporal Difference refers to the fact that the Q-Learning function caluclates the Q-Value of a given state-action pair by adding the diminsihed value of the next best state. This is because reinforcement learning seeks to maximize the cumulative reward over an episode (value) which can not be seen given a state. Temporal Difference approach mathematically estimates this value. Finally, Off Policy simply means that our algorithm does not consider an optimal behaviour when considering the next best action. 

```
    ALPHA = 0.9 #This is the learning rate
    GAMMA = 0.99 #This is the discount factor
    EPS = .4 #e - greedy value (perecent probability it will pick the optimal state-action pair)

    Q = {}
    for state in env.stateSpacePlus:
        for action in env.actionSpaceNum:
            Q[state, action] = 0 #table of state and action pairs for our Q Learning

    numComp = 1500 #The number of episodes and time that the while loop below will be entered
    totalRewards = np.zeros(numComp) 
    for i in range(numComp): #constantly iterate through all desired episodes
        if i % 100 == 0:
            print('Starting Composition ', i) #This will print every every 100 episodes
    
        done = False
        epRewards = 0
        observation = env.reset()

        n = 0 #initialize n
        Z = [] #initialize z dictionary of selected actions

        while not done: #This loop will not stop until the episode is done which is determined by the isTerminal function in the environment
            n = n + 1
            rand = np.random.random() #This returns a random number between 0 and 1 
            action = maxAction(Q,observation, env.actionSpaceNum) if rand < (1-EPS) \
                                else env.actionSpaceSample() #This is an e-greedy policy that selects all the best actions once a threshold is reached decided by epsilon. This is a way of balancing between exploration and exploitation. The more random actions (exploration) the more it COULD potentially learn better approaches.
            
            Z.append(env.actionSpaceDic[action]) #This will append every index to a list for later use
            
            observation_, reward, done, info = env.step(n, env.actionSpaceDic[action]) #observation in this code is the same as state
            epRewards += reward
   
            action_ = maxAction(Q, observation_, env.actionSpaceNum) #Finds the next best action in the future state in order to calculate below a more precise estimation for the current state, action pair

            Q[observation,action] = Q[observation,action] + ALPHA*(reward + \
                        GAMMA*Q[observation_,action_] - Q[observation,action]) #This function is the root of Q-Learning, This is the constant update of Q to find the most precise value for the state action pair given the state action pair after that
            observation = observation_
            
        if EPS - 2 / numComp > 0:
            EPS -= 2 / numComp
        else:
            EPS = 0
        totalRewards[i] = epRewards
```

#### Reward Function
It would've been infeasible to create an effective reward function based on general musci theory due to its intractible breadth. Therfore I chose to construct a reward function solely on jazz harmonic theory. My reward function penalized the agent if it picked a chord whos root didn't match that of the baseline or didn't follow conventional voice leading rules. The maximum amount of points that agent could acquire over an episode is 8. 

### Results
![Figure_1](https://user-images.githubusercontent.com/84595669/187099460-7961f601-67f0-49a4-ad72-58478871a967.png)

The loss function shows that the model is learning the best chords to select which is promising. However the music does not sound aesthetically pleasing. In analyzing the sheet music, the chords are extremely close together and show essentially no signs of variation. In addition, the roots of the chosen chord do not match with the given baseline in the environment. This most likely means there is a problem or insufficiency with the reward function, as this function essentially outlines desired outcomes. 

### Conclusions
Because music requires perfection in note choice, sub optimal results, even if they are high accuracy will not translate well into producable/useful music. The E-greedy in this current implementation works well as seen through a end value score of 0, which is the maximum score the agent can recieve. Therefore, next steps would be to ensure that the reward function is completely outlining the desired results and it results in a tractible algorithm. I speculate that revisiting and refining the reward function would also require a more complex solution to the exploration/exploitation problem as the number of optimal solution would decrease. Nevertheless, Reinforcement Learning shows promise in music generation, however optimal results requires careful construction of its reward function.

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
Music composition is a widely studied field of music. When a music composer first sits down to write a piece of music, it is commonly practice to first consider the emotions you are trying to evoke from the listener. Ultimately, it is the response to this question that will ultimately guide the composer throughout the entire music composition process as every decision made will enforce this. Understanding that this question is not considered but rather bypassed completely by a machine learning model begs the question, "How can emotion in music be quantified?". For composers, one of the biggest ways of influencing the listener's emotions is by utilizing harmonic tension and resolution. Moreover, there are objective measures of harmonic tension as developed by researchers that prove accurate. Given a function that passes any chord (or chords) adn returns tension values (scalar), I created a new chord vector vocabulary using a classification model (binary chords as the categories and tension values as the labels) and extracting the embedding layer. Now I am currently empoying a generative model to analyze the differences in music composition using a binary chord vocabulary and my embedding chord vocabulary.

#### Psychoacoustic Dissonance
Helmholtz in the late 1800's, and later Plomp and Levelt in the mid 1900's determined that an objective measure of harmonic tension can be measured by analyzing the harmonics of two or more signals in relation to eachother. This method was codified into a dissonance function by William Sethares in the early 2000's that passes in two frequency spectrums of equal length and returns a dissonance value. In summary, this theory states that there is a harmonic tension and the beat frequency between a signals harmonics are directly proportional. 

```
# The dissonance function as codified by William Sethares in the early 2000's - built on the previous research conducted by Helmholtz, Plomp and Levelt.
def dissmeasure(fvec, amp, model='min'):
    
    # Sort by frequency
    sort_idx = np.argsort(fvec)
    am_sorted = np.asarray(amp)[sort_idx]
    fr_sorted = np.asarray(fvec)[sort_idx]

    # Used to stretch dissonance curve for different freqs:
    Dstar = 0.24  # Point of maximum dissonance
    S1 = 0.0207
    S2 = 18.96

    C1 = 5
    C2 = -5

    # Plomp-Levelt roughness curve:
    A1 = -3.51
    A2 = -5.75

    # Generate all combinations of frequency components
    idx = np.transpose(np.triu_indices(len(fr_sorted), 1))
    fr_pairs = fr_sorted[idx]
    am_pairs = am_sorted[idx]

    Fmin = fr_pairs[:, 0]
    S = Dstar / (S1 * Fmin + S2)
    Fdif = fr_pairs[:, 1] - fr_pairs[:, 0]

    if model == 'min':
        a = np.amin(am_pairs, axis=1)
    elif model == 'product':
        a = np.prod(am_pairs, axis=1)  # Older model
    else:
        raise ValueError('model should be "min" or "product"')
    SFdif = S * Fdif
    D = np.sum(a * (C1 * np.exp(A1 * SFdif) + C2 * np.exp(A2 * SFdif)))

    return D
```

#### Dissonance Curve
Using the dissonance function outlined above, I created a dissonance graph for every interval between unison and an octave inclusive (graph on the left). Interestingly enough, every local minimum in the interval dissonance graph is a tone in the western chromatic scale. This point was made by William Sethares upon discovering this graph. Nevertheless, this function can be extended to 3 note (top graph) and 4 note (bottom graph) dissonance graphs. I then used these graphs to map the harmonic tension across a piece of sheet music (right graph). The training corpus I used to create tension graphs with were Bach chorales. 

![DIssonance Curve Flow Chart](https://user-images.githubusercontent.com/84595669/188961931-74bf63b5-cda7-4e01-a1f6-6694bab8d15a.png)

#### Embedding
I constructed a Multilayer Perceptron incorporating an embedding layer to predict the dissonance values of all possible binary chord vector representations. After the model overfit to the data (this is desirable because we don't want it to generalize), I extracted the embedding layer and performed some dimensionality reduction techniques to obtain the graph below. The x and y axis for this graph are purely positional and relative. Note that there are noticeable clusters of certain chords due to their similar dissonance values. 

![image](https://user-images.githubusercontent.com/84595669/192071956-6e76fb32-c069-4cbc-bd5c-0c33c87e49fc.png)

#### Transformer and Music Generation
Currently in Progress...

### Results and Conclusion
Currently in Progress...

### Poster
![Machine Learning Composing Music Utilizing Frequency Theory pptx](https://user-images.githubusercontent.com/84595669/187098383-ebdfc6a3-73e7-4f1c-9d07-ac7b98ba280c.png)

### Citations
- References: Helmholtz H. Dover Publications; New York, NY: 1877. On the sensations of tone as a physiological basis for the theory of music. 
- Plomp, R., & Levelt, W. J. M. (1965). Tonal consonance and critical bandwidth. The journal of the Acoustical Society of America, 38(4), 548-560.
- Sethares, W. A. (1993). Local consonance and the relationship between timbre and scale. The Journal of the Acoustical Society of America, 94(3), 1218-1228.
- Yoo, M. J., & Lee, I. K. (2006, November). Musical Tension Curves and its Applications. In ICMC.
