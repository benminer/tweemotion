import * as R from 'ramda';
import * as React from 'react';

import { Text } from 'react-native';

// declare let global: {
//     document: any
// };

let Icon = R.always(Text);

// This lets us use different icon components depending on whether we are
// running the app or running storybook components. Expo has its own icon
// library that we don't have access to from the outside.
export const setIconComponent = (Cmp) => {
    Icon = Cmp;
};

export const getIconComponent = (isNative) => props => {
    const style = (props.reverse && isNative) ? {
        ...props.style,
        transform: [{
            rotate: '180deg'
        }, {
            rotateX: '180deg'
        }],
    } : props.style;

    return <Icon {...props} style={style} />;
};

export const IconWrapper = props => {
    const MainIcon = getIconComponent(!global.document);

    const styles = {
        ...props.style,
        color: (typeof props.style.color === 'function') ?
            props.style.color(props) :
            props.style.color
    };

    return (
        <Text style={styles}>
            <MainIcon name={props.name} {...props} style={styles} />
        </Text>
    );
};

export default IconWrapper;