import { Dimensions } from 'react-native';

const Responsive = props => {
    const { width } = Dimensions.get('window');
    const { minWidth = 0, maxWidth = Infinity } = props;

    return (
        minWidth <= width &&
        maxWidth >= width
    ) ? props.children : null;
};

export default Responsive;