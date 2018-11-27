import Main from '../Components/Main';
import { path } from 'ramda';
import { compose, withState, withHandlers } from 'recompose';
import { curry } from 'ramda';
import { api } from '../api'

const submitHashtag = curry((props, _e) => {
    props.setIsLoading(true);
    if (props.enteredTweetText) {
        api.post('/tweets', { query: props.enteredTweetText })
            .then(res => {
                const response = path(['data', 'results'], res);
                const newChartData = {
                    labels: [
                        'Negative',
                        'Neutral',
                        'Positive'
                    ],
                    datasets: [{
                        data: [response.negative, response.neutral, response.positive],
                        backgroundColor: [
                            '#FF6384',
                            '#36A2EB',
                            '#FFCE56'
                        ],
                        hoverBackgroundColor: [
                            '#FF6384',
                            '#36A2EB',
                            '#FFCE56'
                        ]
                    }]
                };
                props.setChartData(newChartData);
                props.setIsLoading(false);
                props.setShowChart(true);
            })
    }
});

const submitText = curry((props, _e) => {
    props.setIsLoading(true);
    if (props.enteredText) {
        api.post('/predict_tweet', {
            tweet: props.enteredText
        })
            .then(res => {
                const response = path(['data', 'sentiment'], res);
                props.setTextSentiment(response);
                props.setShowTextResponse(true);
                props.setIsLoading(false);
            });
    }
});

const resetField = curry((props, _e) => {
    props.setTextSentiment('');
    props.setEnteredTweetText('');
    props.setEnteredText('');
    props.setShowTextResponse(false);
    props.setShowChart(false);
});

const onChangeText = curry((props, e) => props.setEnteredText(e))

const onChangeTweetText = curry((props, e) => props.setEnteredTweetText(e));

const showAboutText = curry((props, _e) => {
    props.setShowAbout(true);
});

const showTryItOut = curry((props, _e) => {
    props.setShowChart(false);
    props.setShowAbout(false);
});

const data = {
    labels: [
        'Red',
        'Green',
        'Yellow'
    ],
    datasets: [{
        data: [27, 12, 11],
        backgroundColor: [
            '#FF6384',
            '#36A2EB',
            '#FFCE56'
        ],
        hoverBackgroundColor: [
            '#FF6384',
            '#36A2EB',
            '#FFCE56'
        ]
    }]
};

const MainLogic = compose(
    withState('chartData', 'setChartData', data),
    withState('isLoading', 'setIsLoading', false),
    withState('showChart', 'setShowChart', false),
    withState('showAbout', 'setShowAbout', false),
    withState('showTextResponse', 'setShowTextResponse', false),
    withState('enteredText', 'setEnteredText', ''),
    withState('enteredTweetText', 'setEnteredTweetText', ''),
    withState('textSentiment', 'setTextSentiment', ''),
    withHandlers({
        submitHashtag,
        submitText,
        showAboutText,
        showTryItOut,
        onChangeText,
        onChangeTweetText,
        resetField
    })
)(Main);

export default MainLogic;