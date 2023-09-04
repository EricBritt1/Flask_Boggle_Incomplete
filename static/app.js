// Prevent form from refreshing
$('#form').submit(function(e){
    e.preventDefault();
    const word = $('#user_guess').val()
    // Don't forget to pass user_input into check_word. We'll call that function inside of this one!
    check_word(word)
});


async function check_word(word) {
    // I don't understand the {paramas: {word: word}} portion of the get request. What is that doing? Is this supposed to be {jsonify {'result' : response}}
    const res = await axios.get('http://127.0.0.1:5000/check', {params: {word: word}});
    console.log(res)
}

