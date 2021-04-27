document.addEventListener('DOMContentLoaded', function() {
    showAnswerButtons = document.querySelectorAll('.show-answer')
    showAnswerButtons.forEach(element => {
        element.addEventListener('click', function() {
            handleShowAnswer()
        })
    });
})

function handleShowAnswer() {
    answer = document.getElementById(`answer-${event.target.id}`)
    if (answer.style.display === 'block') {
        answer.style.display = 'none'
        event.target.innerHTML = 'Show answer'
    } else {
        event.target.innerHTML = 'Hide answer'
        //event.target.style.display = 'none'
        answer.style.display = 'block'
    }
}

