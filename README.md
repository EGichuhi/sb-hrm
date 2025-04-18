<div align="center">
	<a >
		<img src="/frappe/sb-hrm/frontend/public/favicon.png" height="128" alt="Frappe HR Logo">
	</a>
	<h2>Frappe HR</h2>
	<p align="center">
		<p>Open Source, modern, and easy-to-use HR and Payroll Software for all organizations</p>
	</p>

[![CI](https://github.com/frappe/hrms/actions/workflows/ci.yml/badge.svg?branch=develop)](https://github.com/frappe/hrms/actions/workflows/ci.yml)
[![codecov](https://codecov.io/gh/frappe/hrms/branch/develop/graph/badge.svg?token=0TwvyUg3I5)](https://codecov.io/gh/frappe/hrms)

[https://frappehr.com](https://frappehr.com)

<div align="center" style="max-height: 40px;">
	<a href="https://frappecloud.com/hrms/signup">
		<img src=".github/try-on-f-cloud-button.svg" height="40">
	</a>
</div>

</div>

## Installation

### Manual Installation

1. [Install bench](https://github.com/frappe/bench).
2. [Install ERPNext](https://github.com/frappe/erpnext#installation).
3. Once ERPNext is installed, add the hrms app to your bench by running

	```sh
	$ bench get-app hrms
	```
4. After that, you can install the hrms app on the required site by running
	```sh
	$ bench --site sitename install-app hrms
	```

## License

GNU GPL V3. (See [license.txt](license.txt) for more information).

The HR code is licensed as GNU General Public License (v3) and the copyright is owned by Frappe Technologies Pvt Ltd (Frappe) and Contributors.
