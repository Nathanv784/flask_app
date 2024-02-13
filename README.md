# FLASK CRUD APPLICATION
This is simple Flask CRUD(Create, Read, Update, Delete) Application for User and Note 
## Prerequisites
**1. install python**
   - Download and install Python from [here](https://www.python.org/downloads/).

**2.Create  PostgreSQL Database**
- Install PostgreSQL from [here](https://www.postgresql.org/download/).

**3.install pgAdmin4**
   - Download and install pgAdmin4 from [here](https://www.pgadmin.org/download/).

**4.install Postman**
   - Install PostgreSQL from [here](https://www.postgresql.org/download/).

## Clone Repository
<pre><code> git clone [repository_url]</pre></code>

## Setting Virtual environment
**1.install Virtual environment**
<pre><code>sudo apt install python3.8-venv</pre></code>
**2.Create a Virtual Environment**
 
   - For Linux/Mac
      <pre><code>python3 -m venv envname</code></pre>
- For Windows
      <pre><code>python -m venv envname</code></pre>

**3.Activate virtual environment**
   - For Linux/Mac
      <pre><code>source envname/bin/activate</code></pre>

      -  For Windows
      <pre><code>.\envname\Scripts\activate</code></pre>
**4.install Dependencies**
     <pre><code>pip install -r requirements.txt</pre></code> 
 
**5.Initialize the database:**
 <pre><code>flask db init</pre></code>
 <pre><code>flask db migrate -m "Initial migration"</pre></code>
 <pre><code>flask db upgrade</pre></code>

**6.Run the Application**

  <pre><code>python3 app.py</code></pre>

**7.Deactivate the Virtual Environment**

<pre><code>deactivate</code></pre>


