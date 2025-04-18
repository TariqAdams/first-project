// Add to MathGame class
saveProgress() {
    localStorage.setItem('mathGame', JSON.stringify({
        level: this.level,
        score: this.score,
        questionsAnswered: this.questionsAnswered
    }));
}

loadProgress() {
    const saved = localStorage.getItem('mathGame');
    if (saved) {
        const data = JSON.parse(saved);
        this.level = data.level;
        this.score = data.score;
        this.questionsAnswered = data.questionsAnswered;
        this.updateDisplay();
    }
}
