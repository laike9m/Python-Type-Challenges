

class PassedState {

    _key = 'passedState';
    state = null;

    constructor(initialState = {}) {
        const currentState = localStorage.getItem(this._key);
        // initialize the state when there is no state in the local storage.
        if (!currentState && !initialState) {
            throw new Error('initial state is required when there is no state in the local storage.');
        }

        // add passed property to the challenges in the initial state.
        const rawState = this._prepareState(initialState);

        // check new state and old state whether is undefined or not. and merge the new state to the old state.
        const state = this._checkAndMerge(rawState, currentState);
        this._save(state);
        this.state = state;
        return
    }

    /**
     * prepare the state for initialization.
     * @param {object} rawState 
     * @returns state - the state contains the challenge name and whether the challenge is passed.
     */
    _prepareState(rawState) {
        if (!rawState) {
            return {};
        }

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

    get() {
        return this.state;
    }

    _save(state) {
        localStorage.setItem(this._key, JSON.stringify(state));
    }

    /**
     * Set the challenge as passed in the state.
     * @param {'basic' | 'intermediate' | 'advanced' | 'extreme'} level - the level of the challenge.
     * @param {string} challengeName - the name of the challenge.
     * @returns void
     */
    setPassed(level, challengeName) {
        const challenges = this.state[level];
        for (const challenge of challenges) {
            if (challenge.name === challengeName) {
                challenge.passed = true;
                break;
            }
        }

        this._save(this.state);
    }

    /**
     * Merge the new state to the current state. this function will compare the new state with the current state and finally overwrite the current state based on the new state: 
     * - If the old key in the current state is not in the new state, the old key will be removed from the current state. 
     * - If the new key in the new state is not in the current state, the new key will be added to the current state.
     * @param {object} newState 
     */
    _checkAndMerge(newState, oldState) {
        if (!newState && !oldState) {
            throw new Error('one of the new state and the old state is required.');
        }

        if (!newState) {
            return oldState;
        }
        // TODO: compare the new state with the old state and merge the new state to the old state.
    }
}