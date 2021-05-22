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
    document.querySelectorAll('.ignore-question').forEach(element => {
        element.addEventListener('click', handleIgnoreQuestion)
    })
    document.querySelectorAll('.hide-question').forEach(element => {
        element.addEventListener('click', handleHideQuestion)
    })
})

function handleHideQuestion() {
    questionId = event.target.dataset.id.split('-')[2]
    document.getElementById('question-' + questionId).style.display = 'none'
}

function handleIgnoreQuestion() {
    console.log('inHandleIgnore')
    var button = event.target
    var days = event.target.dataset.ignoreFor
    var dataId = event.target.dataset.id.split('-')
    var questionId = dataId[dataId.length - 1]
    fetch(`/api/v1/ignore/${questionId}?days=${days}`, {
        method: 'PATCH',
        credentials: 'same-origin',
        headers: {
            'X-CSRFToken': getCookie('csrftoken')
        }
    })
    .then(function(response) {
        console.log(response.status)
        return response.json()
    })
    .then(function(data) {
        var untilDate = new Date(`${data['ignore_until']}`).toLocaleDateString()
        console.log(button)
        button.classList.remove('btn-warning')
        button.classList.add('btn-success')
        if (days === "indefinitely") {
            button.innerHTML = `Ignored indefinitely. Click to hide question. You must visit the admin to unhide this question.`
        } else {
            button.innerHTML = `Ignored until ${untilDate}; click to hide question`
        }
        button.removeEventListener('click', handleIgnoreQuestion)
        button.addEventListener('click', handleDismissQuestion)
    })
}

function handleDismissQuestion() {
    button = event.target
    ignoreQuestionX = button.dataset.id.split('-')
    questionId = ignoreQuestionX[1] + '-' + ignoreQuestionX[2]
    document.getElementById(questionId).style.display = 'none'
}

function handleShowAnswer() {
    console.log('inhandleshowancser')
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

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}