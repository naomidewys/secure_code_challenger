<h1>README - Secure Code Challenger</h1>
<h3>Intro</h3
<p>
This brute force security code challenger game was a project created during the <a href="https://www.codelikeagirl.com/" target="_blank">Code Like a Girl</a>: Python 101 Workshop.
It was a short, online workshop that covered an introduction to Python programming and a demonstration of how to apply Python to create a basic code cracking game.
</p>
<h3>Tech Stack</h3>
<ul>
  <li>Python</li>
  <li>VS Code</li>
</ul>
<h3>Features</h3>
<p>
  When using VS Code, the user can click the Python interpreter button. This will open the terminal for the user, and a prompt will appear asking the user to enter the secure 4-digit code.
  Once the user has entered a secure code, the computer will then try to guess the code using brute force.
  A while loop will run until the computer guesses correctly. When the guess is correct, the loop breaks and the terminal will display what the code is and how many guesses it took.
</p>
<h3>Process</h3>
<p>As this was part of an introductory workshop, the instructor walked all attendees through each line with a brief overview (being mindful of time constraints).
The first thing we did was import any necessary elements (e.g., os and random).</p>
<p>Then, we had to define the function to be called.
We gave it a name to output and define the number of guesses and secure code (converting the user's input into an integer to get the 4-digit code).
Then, we established a while loop to randomly generate four numbers to use as guesses and kept a tracker of the number of guesses (adding 1 to each additional guess).</p>
<p>
Then we added an if statement: if guess is equal to secure code, print the code and number of guesses and break the loop.
After the function was defined, we called the function.</p>
<h3>Learnings</h3>
<p>
  The learnings for this project was difficult at first, as the explanations were brief to allow enough time to cover all the material. As I didn't have much experience with Python, 
  I only had a vague grasp of each part; although, I had a clearer understanding when parts overlapped with my JS knowledge (e.g., defining and calling functions).
</p>
<p>
  Since partipating in this workshop, I have completed a Python Developer certificate through <a href="https://www.sololearn.com" target="_blank">Sololearn</a>, which means I have a more thorough understanding
  of each line of code in the project. For example, a while loop is the better option (than for loop) because we don't know how many attempts it would take to crack the code.
  Also, breaking the code will stop an infinite loop from occurring.
</p>
<h3>Improvements</h3>
<p>Here are the improvements I would make as my skills grow:</p>
<ul>
  <li>Each guess can only be made once. Currently, I believe the computer can reguess the same incorrect code. By removing the system's ability to reguess wrong numbers, finding the correct secure code would be faster.</li>
<li>Adding UI. I think it would be a fun challenge to add a visual for the user rather than using the terminal in VS Code.</li>
</ul>
<h3>Image</h3>
<img src="https://github.com/naomidewys/secure_code_challenger/assets/146399253/67318db6-f58c-43d4-b940-d2cd600725d4" alt="secure code entered">
<br>
VS Code terminal prompting the user to enter a code.
<br>
<br>
<img src="https://github.com/naomidewys/secure_code_challenger/assets/146399253/90800c86-14c3-4adc-be1c-0574de6186b4" alt="secure code guessed">
<br>
VS Code terminal after code has been guessed correctly.
