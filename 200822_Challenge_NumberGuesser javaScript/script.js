let humanScore = 0;
let computerScore = 0;
let currentRoundNumber = 1;

// Write your code below:

const generateTarget = () => { return Math.floor(Math.random() * 10) }

const compareGuesses = (humanGuess, computerGuess, targetGuess) => {
    const computerRange = Math.abs(computerGuess - targetGuess)
    const userRange = Math.abs(humanGuess - targetGuess)
    if (userRange <= computerRange) { 
        return true 
    } else {return false}
    
}

const updateScore = (winner) => { winner === 'computer'? computerScore++ : humanScore++ }

const advanceRound = () => { currentRoundNumber++ }
