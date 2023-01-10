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

Create a virtual environment
```shell
python3 -m venv examples
source examples
```

Install dependencies
```shell
python3 -m pip install -r requirements.txt
```

Run the main program
```shell
python3 main.py
```

## Workflow
We create a simple 2-step workflow that fetches the user details and sends an email.

<table><tr><th>Visual</th><th>Code</th></tr>
<tr>
<td width="50%"><img src="workflow.png" width="250px"></td>
<td>
<pre> 
ConductorWorkflow(
    executor=WORKFLOW_EXECUTOR,
    name='user_notification',
    version=1,
).input_parameters(
    ['userId', 'notificationPref']
).add(
    SimpleTask(
        'get_user_info', 'get_user_info'
    ).input(
        'userId', '${workflow.input.userId}'
    )
).add(
    SimpleTask(
        'send_email', 'send_email'
    ).input(
        'email', '${get_user_info.output.email}'
    )
)
</pre>
</td>
</tr>
</table>


## Worker
Workers are a simple interface implementation. See [workers.py](/examples/worker/workers.py) for more details.

## Executing Workflows

There are two ways to execute a workflow:
1. Synchronously - useful for short duration workflows that completes within a few second.  
2. Asynchronously - workflows that runs for longer period

### Synchronous Workflow Execution

```python
TODO
```

### Asynchronous Workflow Execution

```csharp
WorkflowExecutor#StartWorkflow
```

See [main.py](/examples/main.py) for complete code sample of workflow execution.
