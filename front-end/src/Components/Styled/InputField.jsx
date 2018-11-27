import * as R from 'ramda';
import * as React from 'react';

import styled from 'styled-components/native';

import {
    RED,
    // BLUE,
    BLACK,
    // GRAY
} from '../../Style/Colors';

const InputField = props => (
    <Wrapper style={{
        ...props.style,
        borderColor: 'transparent',
        height: props.height,
        backgroundColor:
            props.error ? RED : 'transparent'
    }}>
        <InputFieldStyle
            {...R.omit(['error'])(props)}
            style={{
                color: props.error ? RED : BLACK,
                padding: 5,
                shadowRadius: 10,
                shadowOffset: { height: 10 },
                shadowColor: BLACK,
                shadowOpacity: 0.7,
                borderRadius: 8
            }}
            onChangeText={text => props.onChangeText(text)}
            placeholderTextColor={ props.error ? RED : 'white' }
            multiline={props.multiline}
        />
    </Wrapper>
);

const InputFieldStyle = styled.TextInput`
    font-size: 18;
    font-family: Ubuntu;
    flex: 1;
    background-color: white;
    opacity: 0.75
    width: 100%;
`;

const Wrapper = styled.View`
    border-width: 1;
    width: 100vw;
    flex: 1;
    align-self: center; 
    justify-content: center;
    align-content: center;
    border-radius: 20;
    marginTop: 40;
    
`;

export default InputField;
