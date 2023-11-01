// The solution must return whether a sentence is a pangram or not. A pangram is a sentence that contains every single letter of the alphabet at least once.

function isPangram(string) {
    let lowerCString = string.toLowerCase();
    lowerCString = lowerCString.replace(/[0-9]/g, '');

    let set = new Set(lowerCString);

    set.delete(" ");
    set.delete(".");
    set.delete(",");

    return (set.size == 26) ? true : false
} 
