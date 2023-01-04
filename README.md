# Python QuickStart Example
This repository contains sample applications that demonstrates the various features of Conductor Python SDK.

## SDK Features
Python SDK for Conductor allows you to:
1. Create workflow using Code
2. Execute workflows
3. Create workers for task execution and framework (TaskRunner) for executing workers and communicating with the server.
4. Support for all the APIs such as
    1. Managing tasks (poll, update etc.),
    2. Managing workflows (start, pause, resume, terminate, get status, search etc.)
    3. Create and update workflow and task metadata
    4. User and event management


### Running Example

> **Note**
Obtain KEY and SECRET from the playground or your Conductor server. [Quick tutorial for playground](https://orkes.io/content/docs/getting-started/concepts/access-control-applications#access-keys)

Export variables
```shell
export KEY=
export SECRET=
export CONDUCTOR_SERVER_URL=https://play.orkes.io/api
```

Run the main program
```python
# TODO
```

## Workflow
We create a simple 2-step workflow that fetches the user details and sends an email.

<table><tr><th>Visual</th><th>Code</th></tr>
<tr>
<td width="50%"><img src="workflow.png" width="250px"></td>
<td>
<pre> 
<!-- TODO -->
</pre>
</td>
</tr>
</table>


## Worker
Workers are implemented as simple interface implementation. See [SimpleWorker.py](src/Examples/Worker/SimpleWorker.py) for details.

## Executing Workflows

### Asynchronous Workflow Execution
```python
# TODO
```

See [Main.py](src/Examples/Main.py) for complete code sample of workflow execution.
