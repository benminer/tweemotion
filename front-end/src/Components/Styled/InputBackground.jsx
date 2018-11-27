import * as React from 'react';

import styled from 'styled-components/native';

import Responsive from './Responsive';

const LoginBackgroundDesktop = styled.View`
    padding-left: 50;
    padding-right: 50;
    padding-top: 40;
    padding-bottom: 40;
    border-radius: 15;
    max-width: 85%;
    width: 400;
`;

const LoginBackgroundMobile = styled.View`
    width: 100%;
    padding-left: 32;
    padding-right: 32;
`;

const Wrapper = styled.View`
    width: 100%;
    justify-content: center;
    align-items: center;
    align-self: center;
`;

const InputBackground = props => (
    <Wrapper>
        <Responsive minWidth={641}>
            <LoginBackgroundDesktop>{props.children}</LoginBackgroundDesktop>
        </Responsive>
        <Responsive maxWidth={640}>
            <LoginBackgroundMobile>{props.children}</LoginBackgroundMobile>
        </Responsive>
    </Wrapper>
);

export default InputBackground;