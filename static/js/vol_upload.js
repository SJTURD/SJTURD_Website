var UploadBox = React.createClass({
	getInitialState: function() {
		return {
			catagory: 0,
			location: 0,
			imageUrl: "",
			complete: false, 
		};
	},
	onCatagoryChange: function(e) {
		this.setState{{catagory: e.target.value}}
	}
	onLocationChange: function(e) {
		this.setState{{location: e.target.value}}
	}
	onImageChange: function(e) {
		this.setState{{imageUrl: e.target.value}}
	}
	handleSubmit: function(e) {
		e.preventDefault();
		formData = {
			"catagory": this.state.catagory,
			"location": this.state.location,
			"imageUrl": this.state.imageUrl,
		};
		$.ajax({
			url: "api/upload",
			method: "POST",
			data: formData,
			dataType: "json",
			success: function(data) {
				console.log(data);
				if (data == true) {
					this.setState({complete: true});
				} else {
					alert("Error while uploaing :(")
				}
			}.bind(this),
			error: function(xhr, status, err) {
				console.error("api/upload", status, err.toString());
			}.bind(this)
		})
	}
	render: function() {
		return (
			<div className="volUploadDiv">
			<form onSubmit={this.handleSubmit}>
				<label className="volLabel" for="catagory">物品类别</label>
				<select name="catagory" className="volSelect" value={uploadItem.catagory} onChange={this.onCatagoryChange}>
					<option value="0">钥匙</option>
					<option value="1">学生卡</option>
					<option value="2">身份证</option>
				</select>
				<label className="volLabel" for="location">现存地点</label>
				<select name="location" className="volSelect" value={uploadItem.location} onChange={this.onLocationChange}>
					<option value="0">一餐一楼服务台</option>
					<option value="1">东上院一楼杂货铺</option>
					<option value="2">天上</option>
				</select>
				<label className="volLabel" for="image">上传图片</label>
				<input type="text" name="image" onChange={this.onImageChange}>
				<button className="volBtn" type="submit">完成</button>
			</form>
			</div>
		)
	}
})

var UploadList = React.createClass({
	render: function() {
		var uploadList = this.props.data.map(function(uploadItem, idx) {
		return (
	    	<p className="volNumberList">{idx}</p>
			<UploadBox data={uploadItem}/>
		)
	}
});


ReactDOM.render(
  <UploadList />,
  document.getElementById('content')
);