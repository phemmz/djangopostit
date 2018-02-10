import React from "react";
import { connect } from "react-redux";
import * as counterActions from "../actions/counterActions";

import Headline from "../components/Headline";


@connect(state => ({
  counters: state.counters,
}))
export default class SampleAppContainer extends React.Component {
  handleClick() {
    let {dispatch} = this.props;
    dispatch(counterActions.increaseCounter())
  }

  handleApiCall() {
    console.log('heloaowoqhalpap')
    let {dispatch} = this.props;
    dispatch(counterActions.makeApiCall())
  }

  render() {
    let {counters} = this.props
    return (
      <div className="container">
        <div className="row">
          <div className="col-sm-12">
            <Headline>Sample App!</Headline>
            <div onClick={() => this.handleClick()}>INCREASE</div>
            <div onClick={() => this.handleApiCall()}>SuperFucked Miike</div>
            <p>{counters.clicks}</p>
            <p>{process.env.BASE_API_URL}</p>
          </div>
        </div>
      </div>
    )
  }
}
