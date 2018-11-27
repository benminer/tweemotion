import * as React from 'react';
import { Doughnut } from 'react-chartjs-2';
import { View, Text } from 'react-native-web';

const Chart = props => {
    return (
        <View style={{ flex: 1, padding: 10 }}>
            <Text style={{ fontFamily: 'Montserrat-SemiBold', fontSize: 22, textAlign: 'center', color: 'black' }}>
                {props.text}
            </Text>
            { props.showChart && props.isMobile &&
                <Doughnut
                    data={props.data}
                    width={250}
                    height={250}
                    options={{
                        maintainAspectRatio: false
                    }}
                /> 
            }
            { props.showChart && !props.isMobile &&
                <Doughnut
                    data={props.data}
                /> 
            }
            { props.showTextResponse && 
                <Text style={{ fontFamily: 'Montserrat', fontSize: 22, textAlign: 'center', color: 'black' }}>
                    {props.textSentiment}
                </Text>
            }
        </View>
    )
};

export default Chart;