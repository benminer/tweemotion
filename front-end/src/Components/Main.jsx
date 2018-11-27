import * as React from 'react';
import * as R from 'ramda';
import isMobile from '../util/isMobile';

import Button from './Styled/Button';
import ButtonTouchable from './Styled/ButtonTouchable';
import Container from './Styled/Container';
import Center from './Styled/Center';
import Chart from './Chart';
import Header from './Styled/Header';
import InputBackground from './Styled/InputBackground';
import InputField from './Styled/InputField';
import Gradient from './Styled/Gradient';
import { GridWhole } from './Styled/Grid';
import about from '../data/about';

import { View, Text, ActivityIndicator } from 'react-native';

export const preventSubmit =
    R.tap(e => e && e.preventDefault());

const Main = props => {
    const isActiveMobile = isMobile();
    return (
        <Container>
            <Gradient>
            <Header style={{ backgroundColor: 'transparent' }}>
                <View style={{ alignSelf: 'flex-start' }} />
            </Header>
            <Center style={{
                justifyContent: isActiveMobile ? 'flex-start' : 'center',
                backgroundColor: 'transparent',
                paddingTop: isActiveMobile ? 0 : 10
            }}>
                <View style={{ flex: 1, width: '100%', paddingTop: 0, alignContent: 'center' }}>
                    <Text style={{
                        fontFamily: 'Montserrat',
                        fontSize: 25,
                        color: 'white',
                        alignSelf: 'center'
                    }}>
                        Welcome to Tweemotion!
                    </Text>
                    <View style={{ height: 20 }} />
                        <View style={{ flexDirection: 'row', alignSelf: 'center' }}>
                            <ButtonTouchable
                                isLoading={false}
                                onPress={props.showAboutText}
                                style={{
                                    backgroundColor: 'transparent',
                                    alignSelf: 'flex-start',
                                    borderBottomColor: 'white', borderBottomWidth: 0.5,
                                }}
                            >
                                <Text style={{  color: 'white', fontFamily: 'Montserrat', fontSize: 16 }}>
                                    About
                                </Text>
                            </ButtonTouchable>
                            <View style={{ width: 100 }} />
                            <ButtonTouchable
                                isLoading={false}
                                onPress={props.showTryItOut}
                                style={{
                                    backgroundColor: 'transparent',
                                    alignSelf: 'flex-start',
                                    borderBottomColor: 'white', borderBottomWidth: 0.5,
                                }}
                            >
                                <Text style={{ color: 'white', fontFamily: 'Montserrat', fontSize: 16 }}>
                                    Enter Text
                                </Text>
                            </ButtonTouchable>
                        </View>
                    { props.showAbout ?
                        <View 
                            style={{ backgroundColor: 'transparent', alignSelf: 'center', marginTop: 20, alignItems: 'center'  }}
                        >
                            <Text style={{
                                fontFamily: 'Montserrat',
                                fontSize: 18,
                                color: 'white',
                                alignSelf: 'center',
                                alignContent: 'center',
                                textAlign: 'center',
                                marginTop: 5,
                                marginBottom: 30
                            }}>
                                Tweemotion is an AI Research project conducted by Nick Chouard and Ben Miner.
                             </Text>
                            {about.map(section => (
                                <View key={section.title}>
                                    <Text
                                        style={{ 
                                            fontFamily: 'Montserrat-Bold',
                                            fontSize: 25,
                                            color: 'white',
                                            textAlign: 'center',
                                            marginHorizontal: isActiveMobile ? 5 : 10
                                        }}
                                    >
                                        {section.title}
                                    </Text>
                                    <View style={{ height: 10 }} />
                                    <Text
                                        style={{
                                            fontFamily: 'Montserrat',
                                            fontSize: 15,
                                            color: 'white',
                                            textAlign: 'center',
                                            marginHorizontal: isActiveMobile ? 5 : 10,
                                            marginBottom: 10
                                        }}
                                    >
                                        {section.words}
                                    </Text>
                                </View>
                            ))}
                        </View>
                    :
                        props.showChart || props.showTextResponse ?
                            <View>
                                <View style={{ backgroundColor: 'white', borderRadius: 20, margin: 50 }}>
                                    <Chart 
                                        data={props.chartData} 
                                        showChart={props.showChart} 
                                        showTextResponse={props.showTextResponse}
                                        textSentiment={props.textSentiment}
                                        text={props.enteredText || props.enteredTweetText} 
                                        isMobile={isActiveMobile}
                                    />
                                </View>
                                <ButtonTouchable
                                    isLoading={false}
                                    onPress={props.resetField}
                                    style={{
                                        backgroundColor: 'transparent',
                                        alignSelf: 'center',
                                        borderBottomColor: 'white', borderBottomWidth: 0.5,
                                        marginTop: 50,
                                        marginBottom: 100
                                    }}
                                >
                                    <Text style={{ color: 'white', fontFamily: 'Montserrat', fontSize: 16 }}>
                                        Reset
                                    </Text>
                                </ButtonTouchable>
                            </View>
                            :
                            props.isLoading ?
                                <Center style={{ marginTop: 100 }}>
                                    <ActivityIndicator size={50} color='white' />
                                </Center>
                                :
                                <View>
                                    <View style={{ marginTop: 50, alignContent: 'center', justifyContent: 'center' }}>
                                        <InputBackground style={{ backgroundColor: 'transparent' }}>
                                                <Text style={{ textAlign: 'left', fontSize: 15, color: 'white', fontFamily: 'Montserrat'}}>
                                                    Type anything to have its sentiment analyzed!
                                                </Text>
                                            <GridWhole>
                                                <InputField
                                                    height={200}
                                                    multiline={true}
                                                    onChangeText={props.onChangeText}
                                                    placeholder={'Write some text here...'}
                                                    style={{ backgroundColor: 'transparent' }}
                                                />
                                            </GridWhole>
                                        </InputBackground>
                                        <Button
                                            isLoading={false}
                                            onPress={props.enteredText.length && props.submitText}
                                            style={{ marginTop: 50 }}
                                        >
                                            <Text style={{
                                                fontFamily: 'Montserrat',
                                                fontSize: isActiveMobile ? 13 : 20,
                                                top: 20,
                                                marginTop: 10,
                                                color: 'black'
                                            }}>
                                                Submit Custom Text
                                            </Text>
                                        </Button>
                                    </View>
                                    <View style={{ marginTop: 50, alignContent: 'center', justifyContent: 'center' }}>
                                        <InputBackground style={{ backgroundColor: 'transparent' }}>
                                            <Text style={{ textAlign: 'left', fontSize: 15, color: 'white', fontFamily: 'Montserrat' }}>
                                                Enter in a hashtag to analyze 50 tweets containing it.
                                            </Text>
                                            <GridWhole>
                                                <InputField
                                                    height={50}
                                                    multiline={false}
                                                    onChangeText={props.onChangeTweetText}
                                                    placeholder={'Write some text here...'}
                                                    style={{ backgroundColor: 'transparent' }}
                                                />
                                            </GridWhole>
                                        </InputBackground>
                                        <Button
                                            isLoading={false}
                                            onPress={props.enteredTweetText.length && props.submitHashtag}
                                            style={{ marginTop: 50 }}
                                        >
                                            <Text style={{
                                                fontFamily: 'Montserrat',
                                                fontSize: isActiveMobile ? 13 : 20,
                                                top: 20,
                                                marginTop: 10,
                                                color: 'black'
                                            }}>
                                                Submit Twitter Search
                                    </Text>
                                        </Button>
                                    </View>
                                </View>

                    }
                </View>
            </Center>
            </Gradient>
        </Container>
        )
    };
    
    export default Main;
    
    
