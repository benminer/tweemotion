import styled from 'styled-components';
// import { GRADIENT_LEFT, GRADIENT_RIGHT } from '../../Style/Colors';

const Gradient = styled.div`
    width: 100vw;
    height: 100vh;
    overflow-y: scroll;
    background: linear-gradient(149deg, #9d7b7d, #1bd5df);
    background-size: 400% 400%;

    -webkit-animation: AnimationName 18s ease infinite;
    -moz-animation: AnimationName 18s ease infinite;
    animation: AnimationName 18s ease infinite;

    @-webkit-keyframes AnimationName {
        0%{background-position:13% 0%}
        50%{background-position:88% 100%}
        100%{background-position:13% 0%}
    }
    @-moz-keyframes AnimationName {
        0%{background-position:13% 0%}
        50%{background-position:88% 100%}
        100%{background-position:13% 0%}
    }
    @keyframes AnimationName { 
        0%{background-position:13% 0%}
        50%{background-position:88% 100%}
        100%{background-position:13% 0%}
    }
`;

export default Gradient;