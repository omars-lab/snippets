# Default Bash Variables
echo "Defaulting the varaible to ${one-word}"
echo "one = $one"

echo "Guess what, the variable is still not set, so it will still default: ${one:-another word}"
echo "one = $one"

# Default Setting
echo "Setting the varaible to ${two=word}"
echo "two = $two"

echo "Guess what, ${two} is still set, so it wont get re-set: ${two:=YOU SHALL NOT SEE ME}"
echo "two = $two"
