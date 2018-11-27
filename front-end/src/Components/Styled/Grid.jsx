import styled from 'styled-components/native';

const Grid = styled.View`
    flex-direction: row;
    justify-content: space-between;
`;

export const GridHalf = styled(Grid)`
    width: 48%;
`;

export const GridHalfContent = styled(GridHalf)`
    flex-direction: column;
    justify-content: flex-start;
`;

export const GridWhole = styled(Grid)`
    width: 100%;
`;

export const GridWholeContent = styled(GridWhole)`
    flex-direction: column;
`;

export const GridOneFourth = styled(Grid)`
    width: 24%;
`;

export const GridOneThird = styled(Grid)`
    width: 31.5%;
`;

export const GridOneThirdContent = styled(GridOneThird)`
    flex-direction: column;
    justify-content: flex-start;
`;

export const GridTwoThirds = styled(Grid)`
    width: 64.5%;
`;

export const GridTwoThirdsContent = styled(GridTwoThirds)`
    flex-direction: column;
    justify-content: flex-start;
`;
