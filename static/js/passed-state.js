class PassedState {
  _key = 'python-type-challenges';

  /**
   * Initializing when there is no state in the local storage. If there is no state in the local storage, the initial state is required.
   * this function will check the new state and the old state whether is undefined or not and updated the old state based on new state.
   * 
   * @param {object} newState - the initial state of the challenges which grouped by the level.
   * @returns void
   */
  init(newState) {
    const oldState = this.get();
    // initialize the state when there is no state in the local storage.
    if (!oldState && !newState) {
      throw new Error('initial state is required when there is no state in the local storage.');
    }

    // check new state and old state whether is undefined or not. and merge the new state to the old state.
    const state = this._checkAndMerge(oldState, newState);
    this._save(state);
  }

  get() {
    const currentState = localStorage.getItem(this._key);
    return JSON.parse(currentState);
  }

  /**
   * Save the state to the local storage with JSON format.
   * @param {object} state - the state contains the challenge name and whether the challenge is passed.
   */
  _save(state) {
    localStorage.setItem(this._key, JSON.stringify(state));
  }

  /**
   * Set the target challenge as passed in the state.
   * 
   * @param {'basic' | 'intermediate' | 'advanced' | 'extreme'} level - the level of the challenge.
   * @param {string} challengeName - the name of the challenge.
   * @returns void
   */
  setPassed(level, challengeName) {
    let state = this.get();

    const challenges = state[level];
    for (const challenge of challenges) {
      if (challenge.name === challengeName) {
        challenge.passed = true;
        break;
      }
    }

    this._save(state);
  }

  /**
   * Merge the new state and the current state. 
   * this function will compare the new state with the current state and finally overwrite the current state based on the new state: 
   * - If the old key in the current state isn't in the new state, the old key will be removed from the current state. 
   * - If the new key in the new state isn't in the current state, the new key will be added to the current state.
   * 
   * @param {object} oldState - the current state stored in the local storage.
   * @param {object} newState - the latest state from the server.
   * @returns mergedState - the merged state.
   */
  _checkAndMerge(oldState, newState) {
    if (!newState && !oldState) {
      throw new Error('one of the new state and the old state is required.');
    }

    if (!newState && oldState) {
      return oldState;
    }

    const state = {};
    for (const level in newState) {
      const challenges = [];
      for (const challengeName of newState[level]) {
        challenges.push({
          name: challengeName,
          passed: false
        });
      }
      state[level] = challenges;
    }

    if (!oldState && newState) {
      return state;
    }

    let mergedState = {};
    const levels = ['basic', 'intermediate', 'advanced', 'extreme'];

    for (const level of levels) {
      // Initialize an empty array for merged challenges
      let mergedChallenges = [];

      // Create a map for quick lookup of challenges by name
      const oldChallengesMap = new Map(oldState[level].map(challenge => [challenge.name, challenge]));
      const newChallengesMap = new Map(state[level].map(challenge => [challenge.name, challenge]));

      // Add or update challenges from the newState
      for (const [name, newChallenge] of newChallengesMap.entries()) {
        let hasPassed = oldChallengesMap.get(name)?.passed || newChallenge.passed;
        mergedChallenges.push({ ...newChallenge, passed: hasPassed });
      }

      // Set the merged challenges for the current level in the mergedState
      mergedState[level] = mergedChallenges;
    }

    return mergedState;
  }
}

const passedState = new PassedState();
export default passedState;