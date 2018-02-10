import axios from 'axios';

export const INCREASE = "INCREASE"
export function increaseCounter() {
    return {type: INCREASE}
}

export function makeApiCall() {
  return (dispatch) => {
    return axios.get('/api/v2/groups')
    .then((response) => {
      console.log(JSON.stringify(response), '  nnananwqnw')
    });
  };
}