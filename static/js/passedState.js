

class PassedState {
    constructor(initialState = {}) {
        const currentState = localStorage.getItem('passedState');
        // initialize the state when there is no state in the local storage.
        if (!currentState) {
            if (!initialState) {
                throw new Error('initial state is required when there is no state in the local storage.');
            }

            const state = this._prepareState(initialState);
            localStorage.setItem('passedState', JSON.stringify(state));
            this.state = state;
            return;
        }

        if (currentState) {
            this.state = JSON.parse(currentState);
        }
    }

    /**
     * prepare the state for initialization.
     * @param {object} rawState 
     * @returns state - the state contains the challenge name and whether the challenge is passed.
     */
    _prepareState(rawState) {
        const state = {};
        for (const level in rawState) {
            const challenges = [];
            for (const challengeName of rawState[level]) {
                challenges.push({
                    name: challengeName,
                    passed: false
                });
            }
            state[level] = challenges;
        }

        return state;
    }
}