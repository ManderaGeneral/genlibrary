<details open>
<summary><h1>genlibrary</h1></summary>

Missing description.

<details>
<summary><h2>Table of Contents</h2></summary>

<pre>
<a href='#genlibrary'>genlibrary</a>
├─ <a href='#Dependency-Diagram-for-ManderaGeneral'>Dependency Diagram for ManderaGeneral</a>
├─ <a href='#Installation-showing-dependencies'>Installation showing dependencies</a>
├─ <a href='#Information'>Information</a>
├─ <a href='#Attributes'>Attributes</a>
└─ <a href='#Contributions'>Contributions</a>
</pre>
</details>


<details open>
<summary><h2>Dependency Diagram for ManderaGeneral</h2></summary>

```mermaid
flowchart LR
2([library]) --> 4([vector])
1([tool]) --> 2([library])
0([import]) --> 2([library])
0([import]) --> 3([file])
2([library]) --> 3([file])
3([file]) --> 5([packager])
2([library]) --> 5([packager])
click 0 "https://github.com/ManderaGeneral/generalimport"
click 1 "https://github.com/ManderaGeneral/generaltool"
click 2 "https://github.com/ManderaGeneral/generallibrary"
click 3 "https://github.com/ManderaGeneral/generalfile"
click 4 "https://github.com/ManderaGeneral/generalvector"
click 5 "https://github.com/ManderaGeneral/generalpackager"
```
</details>


<details open>
<summary><h2>Installation showing dependencies</h2></summary>

| `pip install`                                                        | `genlibrary`   |
|:---------------------------------------------------------------------|:---------------|
| <a href='https://pypi.org/project/generallibrary'>generallibrary</a> | ✔️             |
</details>


<details open>
<summary><h2>Information</h2></summary>

| Package                                                    | Ver                                           | Latest Release       | Python                                                                                                                                                                                                                                                 | Platform        | Cover   |
|:-----------------------------------------------------------|:----------------------------------------------|:---------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------|:--------|
| [genlibrary](https://github.com/ManderaGeneral/genlibrary) | [0.0.1](https://pypi.org/project/genlibrary/) | 2023-02-10 12:13 CET | [3.8](https://www.python.org/downloads/release/python-380/), [3.9](https://www.python.org/downloads/release/python-390/), [3.10](https://www.python.org/downloads/release/python-3100/), [3.11](https://www.python.org/downloads/release/python-3110/) | Windows, Ubuntu | ❌       |
</details>



<details>
<summary><h2>Attributes</h2></summary>

<pre>
<a href='https://github.com/ManderaGeneral/genlibrary/blob/master/genlibrary/__init__.py#L1'>Module: genlibrary</a>
</pre>
</details>


<details open>
<summary><h2>Contributions</h2></summary>

Issue-creation and discussions are most welcome!

Pull requests are currently not wanted, please discuss with me before investing any time
</details>



<sup>
Generated 2023-02-10 12:13 CET for commit <a href='https://github.com/ManderaGeneral/genlibrary/commit/master'>master</a>.
</sup>
</details>

