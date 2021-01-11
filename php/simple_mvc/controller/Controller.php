<?php
include_once("model/Model.php");

class Controller {
	public $model;

	public function __construct() {
		$this->model = new Model();	
	}

	public function invoke() {
		if(!isset($_GET['book'])) {
			// no special book is requested. we'll show a list of all available books
			$books = $this->model->getBookList();
			include 'view/header.php';
			include 'view/booklist.php';	
			include 'view/footer.php';
		} else {
			//show the requested book
			$book = $this->model->getBook($_GET['book']);
			include 'view/header.php';
			include 'view/viewbook.php';	
			include 'view/footer.php';
		}	
	}
}
