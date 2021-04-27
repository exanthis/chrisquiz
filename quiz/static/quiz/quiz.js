document.addEventListener('DOMContentLoaded', function() {
    showAnswerButtons = document.querySelectorAll('.show-answer')
    showAnswerButtons.forEach(element => {
        element.addEventListener('click', function() {
            handleShowAnswer()
        })
    });
    document.querySelector('#show-all-answers').addEventListener('click', function() {
        handleShowAllAnswers()
    })
})

function handleShowAnswer() {
    answer = document.getElementById(`answer-${event.target.id}`)
    if (answer.style.display === 'block') {
        answer.style.display = 'none'
        event.target.innerHTML = 'Show answer'
        event.target.classList.remove('btn-danger')
        event.target.classList.add('btn-primary')
    } else {
        event.target.innerHTML = 'Hide answer'
        answer.style.display = 'block'
        event.target.classList.add('btn-danger')
        event.target.classList.remove('btn-primary')
    }
}

function handleShowAllAnswers() {
    document.querySelectorAll('.answer').forEach(element => {
        if (element.style.display === 'none') {
            element.style.display = 'block'
            event.target.innerHTML = 'Hide ALL answers'
        } else {
            event.target.innerHTML = 'Show ALL answers'
            element.style.display = 'none'
        }
    });
}