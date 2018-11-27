import * as R from 'ramda';
import * as React from 'react';

import { ActivityIndicator, Animated, Easing } from 'react-native';
import { compose, withHandlers, withState } from 'recompose';

import ButtonTouchable from './ButtonTouchable';
import Icon from './Icon';
import styled from 'styled-components/native';

import {
    BLACK
} from '../../Style/Colors';

export const Button = props => {
    const ButtonWrapper = ButtonContainer;
    const ButtonTextWrapper = ButtonText;
    const iconStyles = {
        fontSize: 18,
        marginRight: 3
    };

    const scale = props.bounceScale.interpolate({
        inputRange: [0, 0.5, 1],
        outputRange: [1, 0.8, 1]
    });

    const isEnabled = (
        props.type !== 'loading' &&
        props.type !== 'disabled'
    );

    return (
        <ButtonTouchable onPress={isEnabled ? R.compose(
            props.onPress,
            R.tap(props.handleOnPress)
        ) : undefined} activeOpacity={1}>
            <Animated.View style={{
                flex: 1,
                transform: [{
                    scale
                }],
                alignItems: 'center'
            }}>
                <ButtonWrapper style={props.style}>
                    <ButtonTextWrapper>
                        {props.icon && (
                            <Icon name={props.icon} style={iconStyles} />
                        )} {props.children}
                    </ButtonTextWrapper>
                    {(props.type === 'loading') && (
                        <LoadingSpacer>
                            <ActivityIndicator size="small" color="#FFFFFF" />
                        </LoadingSpacer>
                    )}
                </ButtonWrapper>
            </Animated.View>
        </ButtonTouchable>
    );
};

const handleOnPress = R.curry((props, _e) => {
    Animated.timing(
        props.bounceScale,
        {
            toValue: 1,
            duration: 150,
            easing: Easing.ease
        }
    ).start(() => {
        Animated.timing(
            props.bounceScale,
            {
                toValue: 0,
                duration: 0,
                easing: Easing.ease
            }
        ).start();
    });
});

const LoadingSpacer = styled.View`
    margin-left: 7;
`;

const ButtonContainer = styled.View`
    border-radius: 10;
    padding-top: 16;
    padding-bottom: 16;
    padding-left: 36;
    padding-right: 36;
    border-width: 0;
    width: 35vw;
    margin-horizontal: 50;
    margin: 0;
    margin-bottom: 12;
    background-color: white;
    cursor: pointer;
    shadow-radius: 8;
    shadow-color: ${BLACK};
    shadow-opacity: 0.7;
    shadow-offset: { height: 10 }
`;

// const ButtonFlat = styled(ButtonContainer)`
//     border-radius: 7;
//     padding-top: 10;
//     padding-bottom: 10;
// `;

const ButtonText = styled.Text`
    font-size: 14;
    line-height: 18;
    font-weight: 700;
    text-align: center;
    color: white;
    font-family: Ubunutu;
`;


// const ButtonLoading = styled(ButtonContainer)`
//     background-color: ${R.path(['theme', 'disabledButtonColor'])};
//     cursor: default;
// `;

// const ButtonContainerMutedLink = styled(ButtonContainer)`
//     background-color: transparent;
// `;

// const ButtonContainerPrimary = styled(ButtonContainer)`
//     background-color: ${R.path(['theme', 'brandColor'])};
//     background-image: ${R.path(['theme', 'primaryButtonGradient'])};
// `;

// const ButtonTextMutedLink = styled(ButtonText)`
//     color: ${R.path(['theme', 'mutedTextColor'])};
// `;

// const ActionButton = styled.View`
//     padding-left: 12;
//     padding-right: 12;
//     padding-top: 12;
//     padding-bottom: 12;
//     width: 100%;
//     flex-direction: row;
//     cursor: pointer;
// `;

// const ActionButtonOutlined = styled(ActionButton)`
//     border-width: 1;
//     border-style: solid;
//     border-color: ${R.path(['theme', 'brandColor'])};
//     border-radius: 35;
// `;

// const ActionButtonText = styled.Text`
//     font-family: ${R.path(['theme', 'defaultFontFamilyBold'])};
//     font-weight: bold;
//     color: ${R.path(['theme', 'linkColor'])};
//     font-size: 14;
// `;

// const ActionButtonDarkText = styled(ActionButtonText)`
//     color: ${R.path(['theme', 'brandColor'])};
// `;

// const ActionButtonOutlinedText = styled(ActionButtonText)`
//     color: ${R.path(['theme', 'brandColor'])};
//     width: 100%;
// `;

export default compose(
    withState('bounceScale', 'setBounceScale', () => new Animated.Value(0)),
    withHandlers({
        handleOnPress
    })
)(Button);