if status is-interactive
    # Commands to run in interactive sessions can go here
end
function fish_greeting

    set -l normal (set_color normal)
    set -l green (set_color 00ff00)
    set -l yellow (set_color F90) # bright amber
    set -l blue (set_color 66ccff)
    set -l gray (set_color 888888)
    set -l purple (set_color cc99ff)

    set powered_msgs \
        "candy!" \
        "rubber bands" \
        "a black hole" \
        logic \
        "electromagnetic cheese" \
        "spaghetti code" \
        "undefined behavior" \
        "coffee and denial" \
        "sheer willpower" \
        "a forgotten `sudo`"

    set idx (random 1 (count $powered_msgs))
    set chosen_msg $powered_msgs[$idx]

    printf "$yellow⚡ This terminal session is powered by %s$normal\n" $chosen_msg
    echo ""

    set quotes \
        "“The only way to learn a new programming language is by writing programs in it.” —Dennis Ritchie" \
        "“Premature optimization is the root of all evil.” —Donald Knuth" \
        "“Talk is cheap. Show me the code.” —Linus Torvalds" \
        "“Any fool can write code that a computer can understand. Good programmers write code that humans can understand.” —Martin Fowler" \
        "“The function of good software is to make the complex appear simple.” —Grady Booch" \
        "“First, solve the problem. Then, write the code.” —John Johnson" \
        "“Code is like humor. When you have to explain it, it’s bad.” —Cory House" \
        "“Simplicity is the soul of efficiency.” —Austin Freeman" \
        "“A good programmer is someone who looks both ways before crossing a one-way street.” —Doug Linder" \
        "“Computers are useless. They can only give you answers.” —Pablo Picasso" \
        "“The best error message is the one that never shows up.” —Anonymous" \
        "“Weeks of coding can save you hours of planning.” —Anonymous" \
        "“If it hurts, do it more often.” —Jez Humble (on CI/CD 😅)" \
        "“There are only two kinds of languages: the ones people complain about and the ones nobody uses.” —Bjarne Stroustrup" \
        "“It’s not a bug — it’s an undocumented feature.” —Old Programmer Proverb"

    set q_idx (random 1 (count $quotes))
    set quote $quotes[$q_idx]

    echo "Thought for the day:$normal"
    string split ' ' $quote | string join ' ' | fold -w 70 -s | sed 's/^/  /' | string replace -r '^  (.*)$' "  $gray\1$normal"
    echo ""
end
source ~/.config/fish/aliases.fish
starship init fish | source
zoxide init fish | source
