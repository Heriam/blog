Title: OpenDaylight AAA Configuration and Practice
Date: 2016-03-21
Tags: SDN, AAA, OpenDaylight

 <div><font face="Times New Roman">
<p><font face="Times New Roman"><b>ODL Version: </b>Lithium-SR3   <br />
<b>Tool Used: </b>Postman    <br />
<b>About: </b>There are few documents about AAA related features of OpenDaylight online. This article is to study AAA related features through Northbound REST API using Postman, in order to explore the possibility of further integrating AAA function into VTN project. 
</font></p>
<hr />
<p><strong>1. OpenDaylight AAA Documentation</strong></p>
<hr />
<ul>
<li><a href="https://wiki.opendaylight.org/view/AAA:Main">Project Main Page</a>    </li>
<li><a href="http://www.hao-jiang.com/extra/aaa/idmlight-apis">AAA REST APIs</a> (<a href="https://docs.google.com/spreadsheets/d/1YYMmK_V5LMAjLGZOEjfKSX0x4Gwb-K5Xuk1wZskwWwY/edit#gid=0">Online Excel</a>)    </li>
<li><a href="https://drive.google.com/file/d/0B1KtwIIbDsZXejZ2LUQxRW1wcUE/edit">Design: Identity &amp; Access Management</a>     </li>
<li><a href="http://www.hao-jiang.com/extra/aaa/actors">Design: AAA Actors</a>     </li>
<li><a href="http://www.hao-jiang.com/extra/aaa/auth-model.svg">Design: Auth Model</a>    </li>
<li><a href="https://raw.githubusercontent.com/opendaylight/aaa/master/aaa-authn-api/src/main/docs/credential_auth_sequence.png">Design: Credential Auth Sequence</a>     </li>
<li><a href="https://raw.githubusercontent.com/opendaylight/aaa/master/aaa-authn-api/src/main/docs/federated_auth_sequence.png">Design: Federated Auth Sequence</a>     </li>
<li><a href="https://raw.githubusercontent.com/opendaylight/aaa/master/aaa-authn-api/src/main/docs/resource_access_sequence.png">Design: Resource Access Sequence</a>      </li>
<li><a href="https://wiki.opendaylight.org/view/AAA:Authorization_Hello_World_Example">Authorization Hello World Example</a>    </li>
</ul>
<hr />
<p><strong>2. Install AAA Features from OpenDaylight CLI</strong></p>
<hr />
<p>1) Run OpenDaylight Conroller. Install AAA Features from OpenDaylight Controller CLI shown as below:  <br />
<br>
<img alt="Install AAA Features from OpenDaylight CLI" src="http://7xq8q3.com1.z0.glb.clouddn.com/aaainstall.jpg" />  <br />
<br> <br />
2) Open OpenDaylight RestConf API Documentation web page:  <br />
<br>
<img alt="OpenDaylight RestConf API Documentation Web Page" src="http://7xq8q3.com1.z0.glb.clouddn.com/odlapidoc.png" />     </p>
<hr />
<p><strong>3. Identity Management Practice Examples with Postman</strong>   <br />
<font size=2>Referring to AAA REST API Documentation</font></p>
<hr />
<p>1) Get all users:     <br>  <br />
<img alt=" opendaylight aaa get all users" src="http://7xq8q3.com1.z0.glb.clouddn.com/getalluser.png" />  <br />
<br>  <br />
2) Get by user id:    <br>  <br />
<img alt="opendaylight aaa get by user id" src="http://7xq8q3.com1.z0.glb.clouddn.com/getbyuserid.png" />  <br />
<br>  <br />
3) Update a specific user:    <br>  <br />
<img alt="opendaylight aaa update an user" src="http://7xq8q3.com1.z0.glb.clouddn.com/updateanuser.png" />    <br />
<br>     </p>
<p>(END)</p></font></div>