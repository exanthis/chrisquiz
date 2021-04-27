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
        element.addEventListener('click', function() {
            handleIgnoreQuestion()
        })
    })
})

function handleIgnoreQuestion() {
    days = event.target.dataset.ignoreFor
    dataId = event.target.dataset.id.split('-')
    questionId = dataId[dataId.length - 1]
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
        console.log(data)
    })
}

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