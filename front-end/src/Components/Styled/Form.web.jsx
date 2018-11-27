import * as React from 'react';

const Form = props => (
    <form {...props}>
        {props.children}
    </form>
);

export default Form;