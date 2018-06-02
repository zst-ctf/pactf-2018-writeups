//// Didn't have time to write elegant code for this one (or maybe it's just a part of the problem to understand the hardcode...)

// start('Hello World!')

function start(string) {
    cached = ""
    setTimeout(function() {
        type('echo ' + string, 30, false, true)
    }, 1000)
}

function update(cached, typed) {
    $('#cached').html(cached)
    if (typed)
        $('#typed').html('')
}

function type(text, speed, dots, without_cursor) {
    $('#cached').html(cached)
    $('#typed').html('')
    var texts;
    if (text.constructor === Array)
        texts = text
    else
        texts = [text]
    $(function() {
    if (without_cursor)
        $('.typed-cursor').hide();
        $('#typed').typed({
            strings: texts,
            typeSpeed: speed,
            callback: function() {
                if (texts[0] === 'oops') {
                    setTimeout(function(){
                        $('.text-body').html('<span style="color:rgb(0, 172, 0)">anonymous@pactf.com </span><span style="color:rgb(142, 134, 0)">~<br></span><span id="cached"></span>$ <span id="typed"></span>')
                        start('Hello World!')
                    }, 100);
                }
                else {
                    if (dots) {   
                        if (texts[0] === '...')
                            cached += texts[0] + ' Done'
                        else if (texts[0] === '.....')
                            cached += texts[0] += ' Error: Very hard task!'
                        update(cached, true)
                    } else
                        response(texts[0]);
                }
            }
        });
    });
}

function write(temp, new_string, response_string) {
    setTimeout(function() {
        $('#typed').append(temp);
        cached += response_string + temp;
        setTimeout(function() {
            type(new_string, 30, false, true);
        }, 800)
    }, 150);
}

function response(text) {
    if (text === 'echo Hello World!') {
        $('.text-body').html("<span style=\"color:rgb(0, 172, 0)\">anonymous@pactf.com </span><span style=\"color:rgb(142, 134, 0)\">~<br></span><span id=\"cached\"></span><span id=\"typed\">$ echo Hello World!</span>")
        write('<br>Hello World!<br><br><span style=\"color:rgb(0, 172, 0)\">anonymous@pactf.com </span><span style=\"color:rgb(142, 134, 0)\">~<br></span>$ ', ['Sorry, couldn\'t figure out why it didn\'t work...', '^300For the last 10 years my team and I have been secretly working on a general artificial intelligence that will solve this problem and give you the key.', 'Let me launch it...', 'python artificial_intelligence.py'], '$ ' + text)
    } else if (text === 'Sorry, couldn\'t figure out why it didn\'t work...') {
        cached += 'python artificial_intelligence.py'
        update(cached, true)
        initialize()
    }
}

function initialize() {
    $('.typed-cursor').animate({opacity: 0});
    setTimeout(function() {
        cached += "<br><br>Initializing"
        update(cached, false)
        type('...', 400, true, true)
        setTimeout(function() {
            cached += "<br>Launching brain module"
            update(cached, false)
            type('...', 300, true, true)
            setTimeout(function(){
                cached += "<br>Looking for hidden messages"
                update(cached, false)
                type('...', 400, true, true)
                setTimeout(function() {
                    cached += "<br>Reading CIA database (not really)"
                    update(cached, false)
                    type('...', 500, true, true)
                    setTimeout(function() {
                        cached += "<br>Enabling cognitive system"
                        update(cached, false)
                        type('.....', 200, true, true)
                        setTimeout(function() {
                            cached += "<br>Giving it a name"
                            update(cached, false)
                            type('...', 300, true, true)
                            setTimeout(function(){
                                launch_artificial_intelligence(true);
                                $('.typed-cursor').hide();
                            }, 1300)
                        }, 1500);
                    }, 2300);
                }, 1900);
            }, 1500);
        }, 1900);
    }, 2000);
}

function append_ai(new_string, type_speed, time) {
    book_content_cached += last_string;
    $('#book_content_cached').html(book_content_cached);
    $('#book_content_typed').html(new_string);
    window.baffle('#book_content_typed', {
        characters: 'abcdefghijklmnopqrstuvwxyz',
        speed: type_speed
    }).start().once().reveal(time, time)
    last_string = new_string;
}

book_content_cached = "";
last_string = "";

// be careful when changing stupid to false or it can produce the key!!!
function launch_artificial_intelligence(stupid) {
    $('.right').animate({
        'background-color': 'rgba(255, 255, 255, 0.75)'
    }, 200);
    $('#header_text').html('Artificial Intelligence');

    if (stupid) {
        setTimeout(function() {
            append_ai('Hi, I can recognize dogs!<br><br>', 100, 300);
            setTimeout(function() {
                $("#dog_container").fadeIn('fast');
                setTimeout(function() {
                    $("#cat_container").fadeIn('fast');
                }, 1500)
            }, 2500);
        }, 100);
    } else {
        setTimeout(function() {
            append_ai('Hi. ', 100, 300)
            setTimeout(function() {
                append_ai('I exploited weaknesses of Facebook to access everybody\'s information...', 50, 300)
                setTimeout(function() {
                    append_ai(' Actually I just asked Mark and he sold it.', 40, 300);
                    setTimeout(function() {
                        append_ai(' Oh well.<br><br>', 40, 300);
                        setTimeout(function() {
                            append_ai('Turned out the most discussed topic was... <br><br>', 40, 300)
                            setTimeout(function() {
                                append_ai('CATS<br><br>', 30, 3000);
                                setTimeout(function() {
                                    append_ai('But that\'s not the key. ', 30, 300);
                                    setTimeout(function() {
                                        append_ai('The key is now stored securely in ("http://ibarakaiev.shpp.me/pactf_s7fj43/key_%d.txt", get_key_number(6, [16, 23, 16, 15, 42, 8])).', 30, 300);
                                    }, 1800)
                                }, 6000)
                            }, 1800)
                        }, 2000);
                    }, 2000);
                }, 3000);
            }, 1800);
        }, 300);
    }
}

// this function returns the number needed to access key_%d.txt
function get_key_number(n, arr) {
    // TODO: implement solution to the following problem

    /**
     * You are given a sequence _s_ consisting of _N_ integers. You can divide it to 
     * two sequences _p_ and _q_ such that every element of your sequence belongs exactly
     * to one of these sequences. 
     *
     * Let _B_ be the sum of elements belonging to _p_, and _C_ be the sum of elements
     * belonging to _C_. Note: if some of the sequences is empty then its sum is 0).
     * What is the maximum possible value of _B_ - _C_ 
     */
}