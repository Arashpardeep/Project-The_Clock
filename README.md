<!doctype html>
<html lang="en">

<head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">

    <title>To Do List</title>
</head>

<body>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <div class="container-fluid">
            <a class="navbar-brand" href="#">To Do List</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse"
                data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false"
                aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                    <li class="nav-item">
                        <a class="nav-link active" aria-current="page" href="#">Home</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#">About</a>
                    </li>
                    <li class="nav-item dropdown">
                        <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button"
                            data-bs-toggle="dropdown" aria-expanded="false">
                            Items
                        </a>
                        <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
                            <li><a class="dropdown-item" href="#">Action</a></li>
                            <li><a class="dropdown-item" href="#">Another action</a></li>
                            <li>
                                <hr class="dropdown-divider">
                            </li>
                            <li><a class="dropdown-item" href="#">Something else here</a></li>
                        </ul>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link disabled">Contact</a>
                    </li>
                </ul>
                <form class="d-flex">
                    <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
                    <button class="btn btn-outline-danger" type="submit">Search</button>
                </form>
            </div>
        </div>
    </nav>

    <div class="container my-4">
        <h2 class="text-center">To Do List</h2>
        <!--text-center is a bootstrap class which takes everything in the center-->

        <div class="form-group">
            <label for="title">Title</label>
            <input type="text" class="form-control" id="title" aria-describedby="emailHelp">
            <small id="emailHelp" class="form-text text-muted">Add an item to the list.</small>
        </div>
        <div class="form-group">
            <label for="description">Description</label>
            <textarea class="form-control" id="description" rows="3"></textarea>
        </div>
        <button id="add" class="btn btn-primary my-4">Add To List</button>
        <button id="clear" class="btn btn-primary my-4" onclick="clearStorage()">Clear List</button>

        <div id="items" class="my-4">
            <h2>Your Items</h2>
            <table class="table">
                <thead>
                    <tr>
                        <th scope="col">S.no.</th>
                        <th scope="col">Item Title</th>
                        <th scope="col">Item Description</th>
                        <th scope="col">Actions</th>
                    </tr>
                </thead>
                <tbody id="tableBody">
                    <tr>
                        <th scope="row">1</th>
                        <td>Get some coffee</td>
                        <td>You need coffee as you are a coder</td>
                        <td><button class="btn btn-sm btn-primary">Delete</button></td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>

    <!-- Optional JavaScript; choose one of the two! -->

    <!-- Option 1: Bootstrap Bundle with Popper -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p"
        crossorigin="anonymous"></script>

    <!-- Option 2: Separate Popper and Bootstrap JS -->
    <!--
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.10.2/dist/umd/popper.min.js" integrity="sha384-7+zCNj/IqJ95wo16oMtfsKbZ9ccEh31eOz1HGyDuCQ6wgnyJNSYdrPa03rtR1zdB" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.min.js" integrity="sha384-QJHtvGhmr9XOIpI6YVutG+2QOK9T+ZnN4kzFN1RtK3zEFEIsxhlmWl5/YESvpZ13" crossorigin="anonymous"></script>
    -->
    <script>

        function getAndUpdate() {
            console.log("Updating List...");
            tit = document.getElementById('title').value;
            desc = document.getElementById('description').value;
            if (localStorage.getItem('itemsJson') == null) {
                itemsJsonArray = [];
                itemsJsonArray.push([tit, desc]);
                localStorage.setItem('itemsJson', JSON.stringify(itemsJsonArray));
            }
            else {
                itemsJsonArrayStr = localStorage.getItem('itemsJson');
                itemsJsonArray = JSON.parse(itemsJsonArrayStr);
                itemsJsonArray.push([tit, desc]);
                localStorage.setItem('itemsJson', JSON.stringify(itemsJsonArray));
            }
            update();
        }

        function update() {
            if (localStorage.getItem('itemsJson') == null) {
                itemsJsonArray = [];
                localStorage.setItem('itemsJson', JSON.stringify(itemsJsonArray));
            }
            else {
                itemsJsonArrayStr = localStorage.getItem('itemsJson');
                itemsJsonArray = JSON.parse(itemsJsonArrayStr);
            }

            //Populating the table
            let tableBody = document.getElementById("tableBody");
            let str = "";
            itemsJsonArray.forEach((element, index) => {
                str += `
                <tr>
                        <th scope="row">${index + 1}</th>
                        <td>${element[0]}</td>
                        <td>${element[1]}</td> 
                        <td><button class="btn btn-sm btn-primary" onclick="deleted(${index})">Delete</button></td>
                    </tr>
                `;
            });
            tableBody.innerHTML = str;
        }

        add = document.getElementById("add");
        add.addEventListener("click", getAndUpdate);
        update();

        function deleted(itemIndex) {
            console.log("Delete", itemIndex);
            itemsJsonArrayStr = localStorage.getItem('itemsJson');
            itemsJsonArray = JSON.parse(itemsJsonArrayStr);
            //Delete itemIndex element from the array
            itemsJsonArray.splice(itemIndex, 1);
            localStorage.setItem('itemsJson', JSON.stringify(itemsJsonArray));
            update();
        }

        function clearStorage() {
            if (confirm("Do you really want to clear the list?")) {
                console.log("Clearing the storage...");
                localStorage.clear();
                update();
            }
        }

        document.body.style.backgroundColor = "pink";
    </script>
</body>

</html>
