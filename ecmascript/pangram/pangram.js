const ALPHABET = 'abcdefghijklmnopqrstuvwxyz'.split('');

class Pangram {
  constructor(sentence) {
    this.sentence = sentence.toLowerCase();
  }

  isPangram() {
    if (this.emptySentence()) {
      return false;
    }
    return this.alphabetInSentence();
  }

  emptySentence() {
    return this.sentence === '';
  }

  alphabetInSentence() {
    const alphabet = new Set(ALPHABET);
    [...this.sentence].forEach(char => alphabet.delete(char));
    return alphabet.size === 0;
  }
}

export default Pangram;
