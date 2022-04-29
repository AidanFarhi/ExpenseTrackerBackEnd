# Expense Tracker Back End

## REST API

Base URL: `exp-tracker/api/v1/`

### User Enpoints
<table>
    <thead>
        <tr>
            <th>Route</th>
            <th>Method</th>
            <th>Params</th>
            <th>Body</th>
            <th>Returns</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>user/get-user</td>
            <td>GET</td>
            <td>user_id</td>
            <td></td>
            <td>{'user_id': int, 'user_name': string}</td>
        </tr>
        <tr>
            <td>user/create-user</td>
            <td>POST</td>
            <td></td>
            <td>{'user_name': string}</td>
            <td>
                Success: {'message': 'success', 'new_user': {'user_id': int, 'user_name': string}}
            <br>
                Error: {'message': 'error'}
            </td>
        </tr>
        <tr>
            <td>user/delete-user</td>
            <td>POST</td>
            <td></td>
            <td>user_id</td>
            <td>{'message': 'success' || 'error'}</td>
        </tr>
    </tbody>
</table>

### Transaction Endpoints
<table>
    <thead>
        <tr>
            <th>Route</th>
            <th>Method</th>
            <th>Params</th>
            <th>Body</th>
            <th>Returns</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>transaction/get-transaction</td>
            <td>GET</td>
            <td>transaction_id</td>
            <td></td>
            <td><br>
            {
                <br>
                &nbsp;&nbsp;'amount': float,
                <br>
                &nbsp;&nbsp;'trans_type': 'expense' || 'income' || 'refund'
                <br>
                &nbsp;&nbsp;'trans_date': timestamp
                <br>
                &nbsp;&nbsp;'user_id': int
                <br>
                &nbsp;&nbsp;'description': string
                <br>
                &nbsp;&nbsp;'category': 'food' || 'housing' || 'utilities' || 'travel' || 'entertainment' ||' pets' || 'essentials'
                <br>
            }
            </td>
        </tr>
        <tr>
            <td>transaction/get-user-transactions</td>
            <td>GET</td>
            <td></td>
            <td>user_id</td>
            <td><br>
            [<br>
            &nbsp;&nbsp;{
                <br>
                &nbsp;&nbsp;&nbsp;&nbsp;'amount': float,
                <br>
                &nbsp;&nbsp;&nbsp;&nbsp;'trans_type': 'expense' || 'income' || 'refund'
                <br>
                &nbsp;&nbsp;&nbsp;&nbsp;'trans_date': timestamp
                <br>
                &nbsp;&nbsp;&nbsp;&nbsp;'user_id': int
                <br>
                &nbsp;&nbsp;&nbsp;&nbsp;'description': string
                <br>
                &nbsp;&nbsp;&nbsp;&nbsp;'category': 'food' || 'housing' || 'utilities' || 'travel' || 'entertainment' ||' pets' || 'essentials'
                <br>
            &nbsp;&nbsp;}
            <br>
            ...
            <br>
            ]
            </td>
        </tr>
        <tr>
            <td>transaction/create-transaction</td>
            <td>POST</td>
            <td></td>
            <td>
            {
                <br>
                &nbsp;&nbsp;'amount': float,
                <br>
                &nbsp;&nbsp;'trans_type': 'expense' || 'income' || 'refund'
                <br>
                &nbsp;&nbsp;'user_id': int
                <br>
                &nbsp;&nbsp;'description': string
                <br>
                &nbsp;&nbsp;'category': 'food' || 'housing' || 'utilities' || 'travel' || 'entertainment' ||' pets' || 'essentials'
                <br>
            }
            </td>
            <td>
                Success: {'message': 'success', 'transaction_id': int}
            <br>
                Error: {'message': 'error'}
            </td>
        </tr>
        <tr>
            <td>transaction/delete-transaction</td>
            <td>POST</td>
            <td></td>
            <td>transaction_id</td>
            <td>{'message': 'success' || 'error'}</td>
        </tr>
    </tbody>
</table>