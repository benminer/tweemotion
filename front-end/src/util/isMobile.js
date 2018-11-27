import { Dimensions } from 'react-native';

const isMobile = () => {
    const { width } = Dimensions.get('window');

    return width < 640;
};

export default isMobile;